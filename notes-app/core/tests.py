from django.test import TestCase
from core.models import Note

class NoteTests(TestCase):
    def test_crud(self):
        self.client.post("/new/", {"title": "Milk", "body": "2L"})
        note = Note.objects.get()
        self.client.post(f"/{note.pk}/edit/", {"title": "Milk", "body": "3L"})
        note.refresh_from_db()
        self.assertEqual(note.body, "3L")
        self.client.get(f"/{note.pk}/delete/")
        self.assertEqual(Note.objects.count(), 0)
