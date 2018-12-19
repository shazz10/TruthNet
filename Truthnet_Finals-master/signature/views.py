from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from . import models
from . import forms
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def homeView(request):
    if request.user.is_authenticated:
        return render(request, 'signature/home.html')
    else:
        return redirect('/login')

def registerView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=forms.userForm(request.POST,request.FILES)
            if form.is_valid():
                useritem = form.save(commit=False)
                useritem.save()
        else:
            form=forms.userForm()
            return render(request, 'signature/register.html',{'form':form})
    else:
        return redirect('/login')

def checkView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=forms.checkForm(request.POST,request.FILES)
            if form.is_valid():
                check_user=form.cleaned_data['userId']
                check_photo=form.cleaned_data['photo']
                filter_photo=model.userInfo.objects.filter(userId=check_user).values('photo')
                base_photo=filter_photo[0]['photo']

        else:
            form=forms.checkForm()
            return render(request,'signature/check.html',{'form':form})
    else:
        return redirect('/login')

def registerUserView(request):
    st=""
    if request.method == "POST":
        if request.user.is_superuser:
            form=forms.userRegisterForm(request.POST)
            if form.is_valid():
                new_email=form.cleaned_data['email']
                new_user_password=form.cleaned_data['password']
                new_confirm_password=form.cleaned_data['ConfirmPassword']
                if(new_user_password==new_confirm_password):
                    new_user=models.UserModel(email=new_email)
                    new_user.set_password(new_user_password)
                    new_user.save()
                    return redirect('/')
                else:
                    st = "password and confirm password does not match"
        else:
            st = "you are not a Super User"
    form=forms.userRegisterForm()
    return render(request,'signature/userRegister.html', {'form': form,'status':st})
