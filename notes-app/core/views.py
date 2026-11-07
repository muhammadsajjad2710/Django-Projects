from django.shortcuts import get_object_or_404, redirect, render
from .models import Note

def note_list(request):
    return render(request, "list.html", {"title": "Notes", "notes": Note.objects.order_by("-id")})

def note_create(request):
    if request.method == "POST":
        Note.objects.create(title=request.POST.get("title", "").strip(), body=request.POST.get("body", "").strip())
        return redirect("list")
    return render(request, "form.html", {"title": "New note", "note": None})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.title = request.POST.get("title", "").strip()
        note.body = request.POST.get("body", "").strip()
        note.save()
        return redirect("list")
    return render(request, "form.html", {"title": "Edit note", "note": note})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect("list")
