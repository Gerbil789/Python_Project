from django.contrib import admin
from .models import Image, Author
from django.utils.html import format_html
from django.contrib.auth.models import User


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'id','author','image_thumbnail')
    def image_thumbnail(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.image.url))

admin.site.register(Image, ImageAdmin)
admin.site.register(Author)


