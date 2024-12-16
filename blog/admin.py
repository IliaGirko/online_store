from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "counted_views",
    )
    list_filter = ("id",)
    search_fields = (
        "title",
        "content",
    )
