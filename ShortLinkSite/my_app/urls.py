from django.urls import path
from .views import PostDetailView, home

urlpatterns = [
    path('', home, name='Home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='Outside'),
]
