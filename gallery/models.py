from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, UserManager
import os
from sorl.thumbnail import ImageField

def get_upload_path(instance, filename):
    return os.path.join("%s" % instance.album.name, filename)

class Album(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = ImageField(upload_to=get_upload_path)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    mod_date = models.DateTimeField('date modified', auto_now=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    tags = models.CharField(max_length=300)

    def __str__(self):
        return self.description

