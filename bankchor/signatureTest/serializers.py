from rest_framework import serializers
from . import models

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.userInfo
        fields = ('photo','userId') 
