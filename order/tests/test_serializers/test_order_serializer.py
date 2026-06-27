import json
from django.test import TestCase
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory
from order.serializers.order_serializer import OrderSerializer

class TestOrderSerializer(TestCase):
    def setUp(self):
        # Cria os dados falsos necessários antes de rodar o teste
        self.user = UserFactory()
        self.product_1 = ProductFactory(price=100)
        self.product_2 = ProductFactory(price=250)
        
        # Cria um pedido associando o usuário e os dois produtos criados acima
        self.order = OrderFactory(user=self.user, product=(self.product_1, self.product_2))
        
        # Passa o pedido criado para o seu Serializer ler
        self.serializer = OrderSerializer(self.order)

    def test_order_serializer_fields_and_total(self):
        # Pega os dados resultantes que o serializer gerou (dicionário Python)
        serializer_data = self.serializer.data

        # 1. Valida se o ID do usuário está correto no JSON gerado
        self.assertEqual(serializer_data['user'], self.user.id)
        
        # 2. Valida se a lista de produtos contém os 2 produtos que adicionamos
        self.assertEqual(len(serializer_data['product']), 2)
        
        # 3. Valida se a sua função get_total() somou corretamente (100 + 250 = 350)
        self.assertEqual(serializer_data['total'], 350)