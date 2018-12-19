from django import forms
from . import models
from django.contrib.auth import get_user_model

class userForm(forms.ModelForm):
    class Meta:
        model=models.userInfo
        fields = ['photo','userId']

class checkForm(forms.Form):
    userId=forms.IntegerField()
    photo=forms.ImageField()

class userRegisterForm(forms.Form):
    email=forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(widget=forms.PasswordInput)
