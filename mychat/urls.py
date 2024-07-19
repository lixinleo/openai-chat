from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="my-index"),
    path("gpt3", views.gpt3),
]
