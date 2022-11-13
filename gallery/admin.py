from django.contrib import admin
from .models import Post, Album

class PostAdmin(admin.ModelAdmin):
    list_display = ('description', 'image', 'pub_date', 'mod_date', 'album', 'tags')
    search_fields = ['description', 'album__name']
    list_filter = ['pub_date', 'mod_date']

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner', 'public', 'pub_date', 'mod_date')
    search_fields = ['name', 'description']
    list_filter = ['pub_date', 'mod_date', 'owner', 'public']

admin.site.register(Post, PostAdmin)
admin.site.register(Album, AlbumAdmin)