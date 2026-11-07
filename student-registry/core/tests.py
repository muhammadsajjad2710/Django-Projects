from django.test import TestCase
from core.models import Student

class StudentTests(TestCase):
    def test_add_student(self):
        self.client.post("/new/", {"name": "Aisha", "email": "aisha@example.com", "course": "CS"})
        self.assertEqual(Student.objects.get().course, "CS")
        self.assertContains(self.client.get("/"), "Aisha")
