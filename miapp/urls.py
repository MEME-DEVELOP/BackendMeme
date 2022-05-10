from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('curso',CursoViewsets)

from django.urls import path,include


urlpatterns = [
    path('api/', include(router.urls))
]