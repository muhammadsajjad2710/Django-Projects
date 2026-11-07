from django.test import TestCase
from core.models import Book

class BookstoreTests(TestCase):
    def test_search(self):
        Book.objects.create(title="Dune", author="Frank Herbert", year=1965)
        Book.objects.create(title="Neuromancer", author="William Gibson", year=1984)
        response = self.client.get("/", {"q": "dune"})
        self.assertContains(response, "Dune")
        self.assertNotContains(response, "Neuromancer")
