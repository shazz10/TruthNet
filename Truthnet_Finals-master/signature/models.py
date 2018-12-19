from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserModelManager(BaseUserManager):

    def create_user(self, email, password=None):

        if not email:
            raise ValueError('User Must Have Email Address')

        email=self.normalize_email(email)
        user=self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):

        user=self.create_user(email, password)

        user.is_superuser=True

        user.save(using=self._db)

class UserModel(AbstractBaseUser, PermissionsMixin):

    email=models.EmailField(max_length=255,unique=True)
    is_staff=models.BooleanField(default=True)

    objects=UserModelManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class userInfo(models.Model):
    photo=models.ImageField(upload_to='images/' , blank=False)
    userId=models.BigIntegerField(primary_key=True, blank=False)
