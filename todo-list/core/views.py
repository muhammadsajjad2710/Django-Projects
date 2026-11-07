from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

def task_list(request):
    return render(request, "list.html", {"title": "Todos", "tasks": Task.objects.order_by("-id")})

def task_add(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(title=title)
        return redirect("list")
    return render(request, "form.html", {"title": "Add task"})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect("list")
