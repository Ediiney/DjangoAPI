from dataclasses import fields
from rest_framework import serializers
from frexco import models

class FrexcoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FrexcoDB
        fields = '__all__'
        
