from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'ProductoD',ProductodViewsets, basename='ProductoD')
router.register(r'ClienteD',ClientedViewsets, basename='ClienteD')
router.register(r'FacturaD',FacturadViewsets, basename='FacturaD')
router.register(r'RegistroD',RegistrodViewsets, basename='RegistroD')
router.register(r'UsuarioD',UsuariodViewsets, basename='UsuarioD')



from django.urls import path,include


urlpatterns = router.urls