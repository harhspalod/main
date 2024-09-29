# donations/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Donation, ChatMessage
from wardrobe.models import Clothes
from django.contrib.auth.decorators import login_required
from datetime import timedelta


def barter_clothes(request, id):
    donation = get_object_or_404(Donation, id=id)
    available_clothes = Clothes.objects.filter(owner=request.user)
    
    if request.method == 'POST':
        barter_cloth_id = request.POST.get('barter_cloth')
        barter_cloth = Clothes.objects.get(id=barter_cloth_id)
        donation.barter_clothes = barter_cloth
        donation.is_completed = True
        donation.save()
        return redirect('community_board')

    return render(request, 'donations/barter_clothes.html', {'donation': donation, 'available_clothes': available_clothes})

def rent_clothes(request, id):
    donation = get_object_or_404(Donation, id=id)
    
    if request.method == 'POST':
        rental_period = int(request.POST.get('rental_period'))
        donation.rental_period = rental_period
        donation.rental_end_date = donation.donation_date + timedelta(days=rental_period)
        donation.is_completed = True
        donation.save()
        return redirect('community_board')

    return render(request, 'donations/rent_clothes.html', {'donation': donation})

def chat_room(request, id):
    donation = get_object_or_404(Donation, id=id)
    chats = donation.chats.all()

    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            ChatMessage.objects.create(donation=donation, sender=request.user, message=message)
        return redirect('chat_room', id=donation.id)

    return render(request, 'donations/chat_room.html', {'donation': donation, 'chats': chats})

def community_board(request):
    available_items = Donation.objects.filter(is_completed=False)
    return render(request, 'donations/community_board.html', {'items': available_items})

def complete_transaction(request, id):
    donation = get_object_or_404(Donation, id=id)
    if request.method == 'POST':
        donation.is_completed = True
        donation.save()
        return redirect('community_board')

def donation_options(request, id):
    cloth = get_object_or_404(Clothes, id=id)
    
    if request.method == 'POST':
        donation_type = request.POST.get('donation_type')
        
        # Create the donation record based on the chosen type
        Donation.objects.create(
            clothes=cloth,
            donor=request.user,
            action=donation_type
        )
        
        # Redirect to the donation listing page
        return redirect('donation_page')
    
    return render(request, 'donations/donation_options.html', {'cloth': cloth})

def donation_page(request):
    donations = Donation.objects.filter(is_completed=False)
    return render(request, 'donations/donation_page.html', {'donations': donations})

def buy_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    # Logic to handle the purchase or claim of the donated item
    return redirect('donation_page')

def buy_donation(request, id):
    donation = get_object_or_404(Donation, id=id)
    
    if request.method == 'POST':
        # Mark the donation as purchased and complete the transaction
        donation.is_completed = True
        donation.save()
        return redirect('donation_page')  # Redirect to the donation listing page
    
    return render(request, 'donations/buy_confirmation.html', {'donation': donation})