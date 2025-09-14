from django.test import TestCase
from ..models import Product, Category

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=10.99,
            category=self.category,
            stock=100
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Test Description')
        self.assertEqual(self.product.price, 10.99)
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.stock, 100)

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_stock_update(self):
        self.product.stock = 50
        self.product.save()
        self.assertEqual(self.product.stock, 50)

    def test_product_category_relationship(self):
        self.assertIn(self.product, self.category.product_set.all())