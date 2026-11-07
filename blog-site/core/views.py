from django.shortcuts import get_object_or_404, redirect, render
from .models import Post

def post_list(request):
    return render(request, "list.html", {"title": "Blog", "posts": Post.objects.order_by("-id")})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "detail.html", {"title": post.title, "post": post})

def post_create(request):
    if request.method == "POST":
        Post.objects.create(title=request.POST.get("title", "").strip(), body=request.POST.get("body", "").strip())
        return redirect("list")
    return render(request, "form.html", {"title": "New post"})
