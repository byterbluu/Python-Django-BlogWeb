from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_category')
    ordering = ('published',)
    search_fields = ('title', 'author__username',)
    list_filter = ('author__username',)
    def post_category(self, obj):
        return ", ".join([c.name for c in obj.category.all().order_by("name")])

# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)