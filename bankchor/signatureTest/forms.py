from django import forms
from . import models

class userForm(forms.ModelForm):
    class Meta:
        model=models.userInfo
        fields = ['photo','userId']

class checkForm(forms.Form):
    userId=forms.IntegerField()
    photo=forms.ImageField()
