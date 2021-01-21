from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from BooksREST.services import IsSuperUser
from .serializers import PurchaseSerializer
from .models import Request


class CreateRequestView(CreateAPIView):
    """Форма создания заявки"""
    permission_classes = (IsAuthenticated,)
    serializer_class = PurchaseSerializer


class RequestsView(APIView):
    """Просмотр заявок"""
    permission_classes = (IsSuperUser,)

    @staticmethod
    def get(request):
        purchase = Request.objects.all()
        serializer = PurchaseSerializer(purchase, many=True)
        return Response({'requests': serializer.data})
