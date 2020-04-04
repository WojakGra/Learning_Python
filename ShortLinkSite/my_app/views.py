from django.views.generic import DetailView
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Post


class PostDetailView(DetailView):
    model = Post
    template_name = 'outside.html'


def home(request):
    return render(request, 'base.html')
