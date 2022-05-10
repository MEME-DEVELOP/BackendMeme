from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'curso',CursoViewsets, basename='curso')
router.register(r'empresa',EmpresaViewsets,basename='empresa')
router.register(r'inventario',InventarioViewsets, basename='inventario')
router.register(r'producto',ProductoViewsets,basename='producto')
router.register(r'proveedor',ProveedorViewsets,basename='proveedor')



from django.urls import path,include


urlpatterns = router.urls