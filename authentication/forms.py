from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='Usuário', max_length=100)
    password = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')
