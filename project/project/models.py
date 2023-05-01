from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default='new user')
    avatar = models.ImageField(default='project/avatars/default.png', null=True, blank=True, upload_to='project/avatars')

    def __str__(self):
        return self.user.username
    
class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project/images')
    description = models.TextField(max_length=1000, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=datetime.now)
    #tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

