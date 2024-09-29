# fashion/admin.py
# admin.py in 'fashion' app
from django.contrib import admin
from .models import FashionBlog

@admin.register(FashionBlog)
class FashionBlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on', 'updated_on']
    search_fields = ['title', 'description', 'author__username']
    list_filter = ['created_on', 'author']
    ordering = ['-created_on']
    date_hierarchy = 'created_on'
    fields = ['title', 'description', 'image', 'author']
    readonly_fields = ['created_on', 'updated_on']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
