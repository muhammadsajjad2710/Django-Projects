from django.test import TestCase
from core.models import ShortLink

class ShortenerTests(TestCase):
    def test_redirect(self):
        self.client.post("/new/", {"code": "docs", "url": "https://example.com/django"})
        response = self.client.get("/go/docs/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "https://example.com/django")
        self.assertEqual(ShortLink.objects.count(), 1)
