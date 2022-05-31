
from django_filters.rest_framework import DjangoFilterBackend
from multiprocessing import context
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
    
class ProductodViewsets(viewsets.ModelViewSet):
    queryset = Productod.objects.all()
    serializer_class=ProductodSerializers

class UsuariodViewsets(viewsets.ModelViewSet):
    queryset = Usuariod.objects.all()
    serializer_class=UsuariodSerializers
    filter_fields=('correo','logo')
        
class RegistrodViewsets(viewsets.ModelViewSet):
    queryset = Registrod.objects.all()
    serializer_class=RegistrodSerializers
    
class FacturadViewsets(viewsets.ModelViewSet):
    queryset = Facturad.objects.all()
    serializer_class=FacturadSerializers
    
class ClientedViewsets(viewsets.ModelViewSet):
    queryset = Cliented.objects.all()
    serializer_class=ClientedSerializers