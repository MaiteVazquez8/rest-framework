from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Roles', viewRoles)
router.register('Usuarios', viewUsuarios)

urlpatterns = [
    path('',Inicio,name="Inicio"),
    path('api/', include(router.urls)),
]