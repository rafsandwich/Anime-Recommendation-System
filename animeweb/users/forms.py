from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False) #require emails?

    class Meta: #nested namespace for configs
        model = User
        fields = ['username', 'email', 'password1', 'password2']
