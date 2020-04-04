from django.db import models


class Post(models.Model):
    link = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.link
