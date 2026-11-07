from django.db.models import Q
from django.shortcuts import redirect, render
from .models import Book

def book_list(request):
    q = request.GET.get("q", "").strip()
    books = Book.objects.all().order_by("title")
    if q:
        books = books.filter(Q(title__icontains=q) | Q(author__icontains=q))
    return render(request, "list.html", {"title": "Bookstore", "books": books, "q": q})

def book_create(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST.get("title", "").strip(),
            author=request.POST.get("author", "").strip(),
            year=int(request.POST.get("year") or 2000),
        )
        return redirect("list")
    return render(request, "form.html", {"title": "Add book"})
