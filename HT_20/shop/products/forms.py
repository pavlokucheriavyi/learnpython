from django import forms
from .models import Products
from django.views.generic import UpdateView


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)





