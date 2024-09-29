from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_clothes, name='add_clothes'),
    path('update/<int:id>/', views.update_clothes, name='update_clothes'),
    path('delete/<int:id>/', views.delete_clothes, name='delete_clothes'),
]
