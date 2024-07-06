from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    nickname = forms.CharField(label='닉네임', max_length=30)
    phone = forms.CharField(label='연락처')
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")