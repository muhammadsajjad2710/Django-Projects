from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product

def product_list(request):
    return render(request, "list.html", {"title": "Inventory", "products": Product.objects.order_by("name")})

def product_create(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST.get("name", "").strip(),
            stock=int(request.POST.get("stock") or 0),
            price_cents=int(request.POST.get("price_cents") or 1),
        )
        return redirect("list")
    return render(request, "form.html", {"title": "Add product"})

def product_sell(request, pk):
    product = get_object_or_404(Product, pk=pk)
    qty = int(request.POST.get("quantity") or 1)
    if product.stock >= qty:
        product.stock -= qty
        product.save()
    return redirect("list")
