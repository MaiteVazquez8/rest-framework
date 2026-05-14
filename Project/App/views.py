from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Función con Parámetros
def Inicio(request):
    return render(request,'Base.html')

class viewUsuarios(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = SerializersUsuarios

class viewRoles(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = SerializersRoles