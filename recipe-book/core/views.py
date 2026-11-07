from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe

def recipe_list(request):
    return render(request, "list.html", {"title": "Recipes", "recipes": Recipe.objects.order_by("title")})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "detail.html", {"title": recipe.title, "recipe": recipe})

def recipe_create(request):
    if request.method == "POST":
        Recipe.objects.create(
            title=request.POST.get("title", "").strip(),
            ingredients=request.POST.get("ingredients", "").strip(),
            steps=request.POST.get("steps", "").strip(),
        )
        return redirect("list")
    return render(request, "form.html", {"title": "New recipe"})
