from rest_framework import generics

from BooksREST.services import IsSuperUser
from . import models
from . import serializers


class UserListView(generics.ListAPIView):
    """Просмотр юзеров"""
    permission_classes = (IsSuperUser,)
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
