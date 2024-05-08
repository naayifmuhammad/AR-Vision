# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))

    business_phone = forms.CharField(
        max_length=15,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
    business_address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "",
                "class": "form-control"
            }
        ))
 

    class Meta:
        model = User
        fields = ('username', 'business_phone', 'business_address', 'email', 'password1', 'password2' )