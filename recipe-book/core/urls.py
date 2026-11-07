from django.urls import path
from . import views
urlpatterns = [
    path("", views.recipe_list, name="list"),
    path("new/", views.recipe_create, name="create"),
    path("<int:pk>/", views.recipe_detail, name="detail"),
]
