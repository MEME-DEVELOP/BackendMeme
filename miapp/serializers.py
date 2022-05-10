from rest_framework import serializers
from .models import *

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Curso
        fields= '__all__'
        
        