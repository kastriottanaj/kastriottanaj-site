from django.contrib import admin
from . models import Post

# Register your models here.


@admin.register(Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'created_at')
