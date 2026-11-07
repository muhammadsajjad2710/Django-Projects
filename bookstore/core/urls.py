from django.urls import path
from . import views
urlpatterns = [
    path("", views.book_list, name="list"),
    path("new/", views.book_create, name="create"),
]
