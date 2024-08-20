from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model


User_model = get_user_model()

class UserRegform(UserCreationForm):
    class Meta:
        model = User_model
        fields = ["username","email","password1","password2"]