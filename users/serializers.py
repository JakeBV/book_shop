from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор юзера"""
    class Meta:
        model = models.CustomUser
        fields = ('id', 'username', 'date_joined')
