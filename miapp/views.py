from django.shortcuts import render
from rest_framework import viewsets
from .models import*
from .serializers import *
# Create your views here.

class CursoViewsets(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class=CursoSerializers
    
    

    
