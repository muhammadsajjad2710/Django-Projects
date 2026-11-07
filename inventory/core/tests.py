from django.test import TestCase
from core.models import Product

class InventoryTests(TestCase):
    def test_sell_reduces_stock(self):
        product = Product.objects.create(name="Mug", stock=5, price_cents=499)
        self.client.post(f"/{product.pk}/sell/", {"quantity": 2})
        product.refresh_from_db()
        self.assertEqual(product.stock, 3)
