from django.shortcuts import render, redirect
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Post
from my_app.utils import random_string_generator


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


def return_link(request, slug):
    if Post.objects.filter(slug=slug).exists():
        link = Post.objects.get(slug=slug)
        return redirect(link.link, permanent=True)
    else:
        return redirect(home, permanent=True)


def home(request):
    if request.method == 'POST':
        if request.POST.get('link'):
            if Post.objects.filter(link=request.POST.get('link')).exists():
                slug_exists = Post.objects.get(link=request.POST.get('link'))
                stuff_for_frontend = {
                    "outside_link":slug_exists.slug,
                }
                return render(request, 'base.html', stuff_for_frontend)

            validate = URLValidator()
            try:
                validate(request.POST.get('link'))
            except ValidationError:
                stuff_for_frontend = {
                    "ValidError":"Enter a valid URL",
                }
                return render(request, 'base.html', stuff_for_frontend)

            post = Post()
            post.link = request.POST.get('link')
            post.slug = slug_generator(Post())
            post.save()

            stuff_for_frontend = {
                "outside_link":post.slug,
            }
            return render(request, 'base.html', stuff_for_frontend)
    return render(request, 'base.html')
