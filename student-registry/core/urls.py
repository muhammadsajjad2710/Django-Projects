from django.urls import path
from . import views
urlpatterns = [
    path("", views.student_list, name="list"),
    path("new/", views.student_create, name="create"),
]
