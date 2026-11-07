from django.shortcuts import get_object_or_404, redirect, render
from .models import Choice, Question

def _poll():
    question = Question.objects.first()
    if question is None:
        question = Question.objects.create(text="Which framework do you prefer?")
        Choice.objects.bulk_create([
            Choice(question=question, text="Django"),
            Choice(question=question, text="FastAPI"),
            Choice(question=question, text="Flask"),
        ])
    return question

def poll_detail(request):
    question = _poll()
    return render(request, "detail.html", {"title": "Poll", "question": question})

def vote(request):
    choice = get_object_or_404(Choice, pk=request.POST.get("choice"))
    choice.votes += 1
    choice.save()
    return redirect("detail")
