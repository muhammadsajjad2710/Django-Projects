from django.test import TestCase
from core.models import Post

class BlogTests(TestCase):
    def test_create_and_list_post(self):
        self.client.post("/new/", {"title": "Hello", "body": "World"})
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get("/")
        self.assertContains(response, "Hello")
        detail = self.client.get(f"/{Post.objects.get().pk}/")
        self.assertContains(detail, "World")
