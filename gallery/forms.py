from urllib import request
from django import forms
from .models import Post, Album

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image', 'tags', 'album']

    def __init__(self, user, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(owner = user)

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'public', 'description']