from django.test import TestCase
from core.models import Issue

class IssueTests(TestCase):
    def test_open_and_close(self):
        self.client.post("/new/", {"title": "Broken login", "description": "500 error"})
        issue = Issue.objects.get()
        self.assertTrue(issue.open)
        self.client.get(f"/{issue.pk}/close/")
        issue.refresh_from_db()
        self.assertFalse(issue.open)
