from django.shortcuts import get_object_or_404, redirect, render
from .models import ShortLink

def link_list(request):
    return render(request, "list.html", {"title": "Short links", "links": ShortLink.objects.order_by("-id")})

def link_create(request):
    if request.method == "POST":
        ShortLink.objects.create(code=request.POST.get("code", "").strip(), url=request.POST.get("url", "").strip())
        return redirect("list")
    return render(request, "form.html", {"title": "New short link"})

def follow(request, code):
    link = get_object_or_404(ShortLink, code=code)
    return redirect(link.url)
