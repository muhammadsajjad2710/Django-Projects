from django.urls import path
from . import views
urlpatterns = [
    path("", views.poll_detail, name="detail"),
    path("vote/", views.vote, name="vote"),
]
