from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Category
from .serializers import ProductSerializer

class ProductViewSetTests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.00,
            category=self.category,
            stock=100
        )
        self.valid_payload = {
            'name': 'New Product',
            'description': 'New Description',
            'price': 15.00,
            'category': self.category.id,
            'stock': 50
        }
        self.invalid_payload = {
            'name': '',
            'description': 'Invalid Product',
            'price': -5.00,
            'category': self.category.id,
            'stock': 50
        }

    def test_create_product(self):
        response = self.client.post(reverse('product-list'), self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(id=2).name, 'New Product')

    def test_create_product_invalid(self):
        response = self.client.post(reverse('product-list'), self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_product(self):
        response = self.client.get(reverse('product-detail', args=[self.product.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product.name)

    def test_update_product(self):
        response = self.client.put(reverse('product-detail', args=[self.product.id]), self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'New Product')

    def test_update_product_invalid(self):
        response = self.client.put(reverse('product-detail', args=[self.product.id]), self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_product(self):
        response = self.client.delete(reverse('product-detail', args=[self.product.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_list_products(self):
        response = self.client.get(reverse('product-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_products(self):
        response = self.client.get(reverse('product-list') + '?category=' + str(self.category.id), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_sort_products(self):
        Product.objects.create(name='Another Product', price=5.00, category=self.category, stock=50)
        response = self.client.get(reverse('product-list') + '?ordering=price', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], 'Another Product')

    def test_paginate_products(self):
        for i in range(10):
            Product.objects.create(name=f'Product {i}', price=10.00, category=self.category, stock=100)
        response = self.client.get(reverse('product-list') + '?page=1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 5)  # Assuming default page size is 5
        self.assertIn('next', response.data)  # Check for pagination key
```