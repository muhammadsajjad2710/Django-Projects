from django.test import TestCase
from core.models import Task

class TodoTests(TestCase):
    def test_add_and_toggle(self):
        self.client.post("/add/", {"title": "Write tests"})
        task = Task.objects.get()
        self.assertFalse(task.done)
        self.client.get(f"/{task.pk}/toggle/")
        task.refresh_from_db()
        self.assertTrue(task.done)
