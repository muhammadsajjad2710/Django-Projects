from django.urls import path
from . import views
urlpatterns = [
    path("", views.link_list, name="list"),
    path("new/", views.link_create, name="create"),
    path("go/<slug:code>/", views.follow, name="follow"),
]
