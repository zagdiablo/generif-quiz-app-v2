from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta(object):
        model = User
        fields = ['username', 'password']

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control'
        }))


class RegistrationForm(UserCreationForm):
    class Meta(object):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your username',
            'class': 'form-control'
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Enter your email',
            'class': 'form-control'
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter your password',
            'class': 'form-control'
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Re-enter your password',
            'class': 'form-control'
        }))
