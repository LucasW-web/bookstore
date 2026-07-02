from django.urls import path, include
from rest_framework import routers
from order.viewsets.order_viewset import OrderViewSet

router = routers.SimpleRouter()
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]