from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="my-index"),
    path("gpt4", views.gpt4, name="gpt4"),
]
