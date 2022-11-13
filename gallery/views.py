from asyncio.windows_events import NULL
from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, UserManager
from .models import Post, Album
from .forms import UploadForm, CreateAlbumForm
import sorl.thumbnail

def base(request):
    return render(request, "base.html")

def display_albums(request):
    if request.method == 'GET' and request.user.is_authenticated:
        albums = Album.objects.filter(owner = request.user)
        return render(request, 'gallery/index.html', {'albums' : albums})
    else:
        raise Http404("The gallery doesn't exist")

def image_upload(request):
    if request.method == 'POST' and request.user.is_authenticated:
        form = UploadForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery:success')
    else:
        form = UploadForm(request.user)
    return render(request, 'gallery/upload.html', {'form' : form})

def success(request):
    return render(request, 'gallery/success.html', {})

def public(request):
    if request.method == 'GET' and request.user.is_authenticated:
        albums = Album.objects.filter(public = True)
        return render(request, 'gallery/public.html', {'albums' : albums})
    else:
        raise Http404("The gallery doesn't exist")

def create_album(request):
    if request.method == 'POST' and request.user.is_authenticated:
        album = Album(owner = request.user)
        form = CreateAlbumForm(request.POST, request.FILES, instance = album)
        if form.is_valid():
            album.save()
            return redirect('gallery:success')    
    else:
        form = CreateAlbumForm()
    return render(request, 'gallery/create_album.html', {'form' : form})

def display_images(request, id):
    try:
        if request.method == 'GET' and Album.objects.get(id = id) in Album.objects.filter(owner = request.user) or Album.objects.filter(id = id).get(public = True):
                posts = Post.objects.filter(album = id)
                album = Album.objects.get(id = id)
                user = request.user
                return render(request, 'gallery/album.html', {'posts' : posts, 'album' : album, 'user' : user})
    except:
        raise Http404("The album doesn't exist")

def delete_image(request, id):
    if request.user.is_authenticated and Post.objects.get(id = id).album in Album.objects.filter(owner = request.user):
        image = Post.objects.get(id = id)
        if request.method == 'POST':
            sorl.thumbnail.delete(image.image)
            image.delete()
            return redirect('gallery:success')
    else:
        raise Http404("You are not the owner")
    return render(request, 'gallery/confirm_image.html', {'image': image})


def delete_album(request, id):
    if request.user.is_authenticated and Album.objects.get(id = id) in Album.objects.filter(owner = request.user):
        album = Album.objects.get(id = id)
        if request.method == 'POST':
            for pic in album.post_set.all():
                sorl.thumbnail.delete(pic.image)
            album.post_set.all().delete()                
            album.delete()
            return redirect('gallery:success')
    else:
        raise Http404("You are not the owner")
    return render(request, 'gallery/confirm_album.html', {'album': album})







