from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.homeView,name='home_page'),
    path('register/',views.registerView,name='register_page'),
    path('check/',views.checkView,name='check_page'),
    path('login/', LoginView.as_view(template_name='signature/login.html'), name="login"),
    path('userreg/',views.registerUserView,name='register_user')

]
