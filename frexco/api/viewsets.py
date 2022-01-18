from rest_framework import viewsets
from frexco.api import serializers
from frexco import models

class FrexcoDBViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FrexcoSerializer
    queryset = models.FrexcoDB.objects.all()    
    
 