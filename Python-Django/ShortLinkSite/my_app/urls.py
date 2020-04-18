from django.urls import path
from .views import return_link, home

urlpatterns = [
    path('', home, name='Home'),
    path('<slug:slug>/', return_link, name='Outside'),
]
