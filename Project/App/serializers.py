from .models import *
from rest_framework import serializers

class SerializersRoles(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class SerializersUsuarios(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'