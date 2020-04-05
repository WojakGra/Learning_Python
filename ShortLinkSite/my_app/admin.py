from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('link', 'slug', 'created')
    search_fields = ['link']


admin.site.register(Post, PostAdmin)
