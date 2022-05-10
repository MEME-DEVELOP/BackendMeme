from rest_framework import serializers
from .models import *

class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Curso
        fields= '__all__'

class EmpresaSerializers(serializers.ModelSerializer):
    class Meta:
        model= Empresa
        fields= '__all__'

class InventarioSerializers(serializers.ModelSerializer):
    class Meta:
        model= Inventario
        fields= '__all__'     
        
class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields= '__all__' 
        
class ProveedorSerializers(serializers.ModelSerializer):
    class Meta:
        model= Proveedor
        fields= '__all__' 