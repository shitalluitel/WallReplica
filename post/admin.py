from django.contrib import admin
from post.models import Post

# Register your models here.

# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'text', 'image', 'is_hidden'
    list_filter = 'is_hidden',
    search_fields = 'text',