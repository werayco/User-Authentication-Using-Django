from django.urls import path, reverse
from . import views


urlpatterns = [
    path("home/", views.index, name="homepage"),
    path("about/<int:id>", views.about, name="about"),
]
