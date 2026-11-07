from django.urls import path
from . import views
urlpatterns = [
    path("", views.task_list, name="list"),
    path("add/", views.task_add, name="add"),
    path("<int:pk>/toggle/", views.task_toggle, name="toggle"),
]
