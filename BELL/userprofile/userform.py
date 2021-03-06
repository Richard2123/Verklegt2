from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserInfo(UserCreationForm):
    email = forms.EmailField(required=True)

    class TheForm:
        model = User
        boxes = ("username", "email", "name", "location", "password1", "password2")