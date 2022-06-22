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
        
class ClientedSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cliented
        fields= '__all__'
        
class FacturadSerializers(serializers.ModelSerializer):
    class Meta:
        model= Facturad
        fields= '__all__'
        
class ProductodSerializers(serializers.ModelSerializer):
    class Meta:
        model= Productod
        fields= '__all__'   
        
class RegistrodSerializers(serializers.ModelSerializer):
    class Meta:
        model= Registrod
        fields= '__all__' 
  
class UsuariodSerializers(serializers.ModelSerializer):
    class Meta:
        model= Usuariod
        fields= '__all__'  