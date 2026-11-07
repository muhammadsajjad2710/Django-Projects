from django.test import TestCase
from core.models import Choice

class PollTests(TestCase):
    def test_vote_increments(self):
        page = self.client.get("/")
        choice = Choice.objects.get(text="Django")
        self.client.post("/vote/", {"choice": choice.pk})
        choice.refresh_from_db()
        self.assertEqual(choice.votes, 1)
        self.assertContains(page, "Which framework")
