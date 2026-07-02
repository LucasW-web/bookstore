import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSetTestCase(APITestCase):
    client = APIClient()

    def setUp(self):
        from django.contrib.auth.models import User
        self.user = User.objects.create_user(username="testuser", password="password")
        
        self.category = CategoryFactory(title='books')
        token = Token.objects.create(user=self.user)

    def test_get_all_category(self):
        token = Token.objects.get(user__username=self.user.username)  # added
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + token.key)  # added
        response = self.client.get(
            reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

        category_data = json.loads(response.content)
        self.assertEqual(category_data[0]["title"], self.category.title)

    def test_create_category(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        data = json.dumps({
            "title": "technology"
        })

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title="technology")

        self.assertEqual(created_category.title, "technology")