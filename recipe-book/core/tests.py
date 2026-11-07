from django.test import TestCase
from core.models import Recipe

class RecipeTests(TestCase):
    def test_create_and_detail(self):
        self.client.post("/new/", {"title": "Chai", "ingredients": "tea, milk", "steps": "boil and steep"})
        recipe = Recipe.objects.get()
        response = self.client.get(f"/{recipe.pk}/")
        self.assertContains(response, "tea, milk")
