from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from order.models import Order
from order.serializers.order_serializer import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Exige que o usuário esteja logado

    def get_queryset(self):
        return Order.objects.all().order_by("id")
