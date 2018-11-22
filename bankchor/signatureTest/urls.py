from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', views.homeView,name='home_page'),
    path('register/',views.registerView,name='register_page'),
    path('check/',views.checkView,name='check_page')
]
