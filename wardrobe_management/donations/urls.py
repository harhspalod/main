from django.urls import path
from . import views

urlpatterns = [
    path('community/', views.community_board, name='community_board'),
    path('barter/<int:id>/', views.barter_clothes, name='barter_clothes'),
    path('rent/<int:id>/', views.rent_clothes, name='rent_clothes'),
    path('chat/<int:id>/', views.chat_room, name='chat_room'),
    path('donate_options/<int:id>/', views.donation_options, name='donate_options'),
    path('donations/', views.donation_page, name='donation_page'),
    path('donations/buy/<int:id>/', views.buy_donation, name='buy_donation'),
    path('donations/confirm_purchase/<int:id>/', views.buy_donation, name='confirm_purchase'),
    path('<int:id>/complete/', views.complete_transaction, name='complete_transaction'),
]
