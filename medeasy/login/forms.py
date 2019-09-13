from django.contrib.auth.models import User
from .models import PatDocUser
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RegisterForm(forms.ModelForm):
    class Meta:
        model = PatDocUser
        fields = ['isDoctor']
