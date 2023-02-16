from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, PasswordInput
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта'
            }),

            "password1": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
            "password2": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Потверждение пароля'
            }),

        }