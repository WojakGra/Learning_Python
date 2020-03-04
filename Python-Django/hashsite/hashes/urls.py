from django.urls import path
from . import views

urlpatterns = [
    path('', views.hashing, name="home"),
]