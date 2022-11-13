from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *


app_name = 'gallery'
urlpatterns = [
    path('', display_albums, name = 'display_albums'),
    path('image_upload', image_upload, name = 'image_upload'),
    path('success', success, name = 'success'),
    path('public', public, name = 'public'),
    path('create_album', create_album, name = 'create_album'),
    path('album/<int:id>', display_images, name = 'album'),
    path('delete_image/<int:id>', delete_image, name='delete_image'),
    path('delete_album/<int:id>', delete_album, name='delete_album')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)