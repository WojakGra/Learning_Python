from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('link', 'slug', 'created')
    search_fields = ['link', 'slug']
    prepopulated_fields = {'slug': ('link',)}


admin.site.register(Post, PostAdmin)
