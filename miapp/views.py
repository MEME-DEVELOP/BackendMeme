from django.shortcuts import render
from rest_framework import viewsets
from .models import*
from .serializers import *
# Create your views here.



class CursoViewsets(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class=CursoSerializers
class EmpresaViewsets(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class=EmpresaSerializers
    
class InventarioViewsets(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class=InventarioSerializers
    
class ProductoViewsets(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class=ProductoSerializers
    
class ProveedorViewsets(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class=ProveedorSerializers