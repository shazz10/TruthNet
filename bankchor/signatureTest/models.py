from django.db import models

# Create your models here.

class userInfo(models.Model):
    photo=models.ImageField(upload_to='images/' , blank=False)
    userId=models.BigIntegerField(primary_key=True, blank=False)
