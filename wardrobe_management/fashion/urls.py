# fashion/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blogs/create/', views.create_blog, name='create_blog'),
    path('blogs/<int:id>/update/', views.update_blog, name='update_blog'),
    path('blogs/<int:id>/delete/', views.delete_blog, name='delete_blog'),
]
