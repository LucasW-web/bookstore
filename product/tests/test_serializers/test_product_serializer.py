from django.test import TestCase
from product.factories import ProductFactory, CategoryFactory
from product.serializers import ProductSerializer

class TestProductSerializer(TestCase):
    def setUp(self):
        # Cria uma categoria fictícia
        self.category = CategoryFactory(title="Eletrônicos")
        # Cria um produto e associa a categoria criada
        self.product = ProductFactory(title="Smartphone", price=1500, category=(self.category,))
        self.serializer = ProductSerializer(self.product)

    def test_product_serializer_fields(self):
        data = self.serializer.data
        
        # Validações básicas do produto
        self.assertEqual(data['title'], "Smartphone")
        self.assertEqual(data['price'], 1500)
        self.assertEqual(len(data['category']), 1)
        self.assertEqual(data['category'][0]['title'], "Eletrônicos")