from django.urls import path
from . import views
urlpatterns = [
    path("", views.issue_list, name="list"),
    path("new/", views.issue_create, name="create"),
    path("<int:pk>/close/", views.issue_close, name="close"),
]
