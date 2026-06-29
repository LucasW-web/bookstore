from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.all().order_by("id")
