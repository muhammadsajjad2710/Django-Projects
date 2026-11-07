from django.urls import path
from . import views
urlpatterns = [
    path("", views.product_list, name="list"),
    path("new/", views.product_create, name="create"),
    path("<int:pk>/sell/", views.product_sell, name="sell"),
]
