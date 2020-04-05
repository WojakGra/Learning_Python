from django.views.generic import DetailView
from django.shortcuts import render
from .models import Post
from my_app.utils import random_string_generator


class PostDetailView(DetailView):
    model = Post
    template_name = 'outside.html'


def slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = random_string_generator()

    slug_class = instance.__class__
    slug_exists = slug_class.objects.filter(slug=slug).exists()
    if slug_exists:
        new_slug = random_string_generator()
        return slug_generator(instance, new_slug=new_slug)
    return slug


def home(request):
    if request.method == 'POST':
        if request.POST.get('link'):
            post = Post()
            if Post.objects.filter(link=request.POST.get('link')).exists():
                slug_exits = Post.objects.get(link=request.POST.get('link'))
                stuff_for_frontend = {
                    "outside_link":slug_exits.slug,
                }
                return render(request, 'base.html', stuff_for_frontend)
            post.link = request.POST.get('link')
            post.slug = slug_generator(Post())
            post.save()

            stuff_for_frontend = {
                "outside_link": post.slug,
            }

            return render(request, 'base.html', stuff_for_frontend)
    else:
        return render(request, 'base.html')