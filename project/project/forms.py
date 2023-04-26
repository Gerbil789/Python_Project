from django.forms import ModelForm
from django import forms
from .models import Image, Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UploadForm(ModelForm):

    
    class Meta:
        model = Image
        fields = ['title', 'image', 'description', 'tags']


class CreateUserForm(UserCreationForm):

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditUserForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        exclude = ['user']