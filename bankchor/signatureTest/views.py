from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from . import serializers
from . import models
from . import forms
import runme
# Create your views here.

def homeView(request):
    return render(request, 'signatureTest/home.html')

def registerView(request):
    if request.method == "POST":
        form=forms.userForm(request.POST,request.FILES)
        if form.is_valid():
            useritem = form.save(commit=False)
            useritem.save()
    else:
        form=forms.userForm()
    return render(request, 'signatureTest/register.html',{'form':form})

def checkView(request):
    if request.method == "POST":
        form=forms.checkForm(request.POST,request.FILES)
        if form.is_valid():
            check_user=form.cleaned_data['userId']
            check_photo=form.cleaned_data['photo']
            filter_photo=model.userInfo.objects.filter(userId=check_user).values('photo')
            base_photo=filter_photo[0]['photo']

            data=[]

            img_base = image.load_img(base_photo, grayscale=True, target_size=(155,220))
            img_base = image.img_to_array(img_base)
            data.append(img_base)

            img_check = image.load_img(check_photo,grayscale=True, target_size=(155,220))
            img_check = image.img_to_array(img_check)
            data.append(img_check)

            x=np.array(data)
            x=runme.format_input(x)

            pair= [[x[0],x[1]]]
            pair=np.array(pair)

            prediction=runme.predict(pair)

            return render(request,'signatureTest/result.html',{'prediction':prediction})
    else:
        form=forms.checkForm()
        return render(request,'signatureTest/check.html',{'form':form})
