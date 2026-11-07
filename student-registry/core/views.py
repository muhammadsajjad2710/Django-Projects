from django.shortcuts import redirect, render
from .models import Student

def student_list(request):
    return render(request, "list.html", {"title": "Students", "students": Student.objects.order_by("name")})

def student_create(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            course=request.POST.get("course", "").strip(),
        )
        return redirect("list")
    return render(request, "form.html", {"title": "Add student"})
