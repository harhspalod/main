# models.py in the 'donations' app
# donations/models.py
from django.db import models
from wardrobe.models import Clothes
from django.contrib.auth.models import User
from datetime import timedelta

class Donation(models.Model):
    ACTION_CHOICES = [
        ('donate', 'Donate'),
        ('trade', 'Trade'),
        ('lend', 'Lend'),
        ('barter', 'Barter'),
        ('rent', 'Rent'),
    ]

    clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, default='donate')
    donation_date = models.DateTimeField(auto_now_add=True)
    recipient_name = models.CharField(max_length=100, null=True, blank=True)
    recipient_contact = models.CharField(max_length=15, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    
    # Barter system
    barter_clothes = models.ForeignKey(Clothes, null=True, blank=True, on_delete=models.SET_NULL, related_name="barter_clothes")
    
    # Rent system
    rental_period = models.PositiveIntegerField(null=True, blank=True)
    rental_end_date = models.DateField(null=True, blank=True)

    def complete_transaction(self):
        self.is_completed = True
        self.save()
        if self.action == 'rent' and self.rental_period:
            self.rental_end_date = self.donation_date + timedelta(days=self.rental_period)

class ChatMessage(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name="chats")
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} on {self.timestamp}"
