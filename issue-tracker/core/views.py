from django.shortcuts import get_object_or_404, redirect, render
from .models import Issue

def issue_list(request):
    return render(request, "list.html", {"title": "Issues", "issues": Issue.objects.order_by("-id")})

def issue_create(request):
    if request.method == "POST":
        Issue.objects.create(title=request.POST.get("title", "").strip(), description=request.POST.get("description", "").strip())
        return redirect("list")
    return render(request, "form.html", {"title": "New issue"})

def issue_close(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    issue.open = False
    issue.save()
    return redirect("list")
