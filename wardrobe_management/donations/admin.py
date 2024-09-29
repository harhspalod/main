
# Register your models here.
# admin.py in 'donations' app
from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['clothes', 'donor', 'donation_date', 'recipient_name']
    search_fields = ['clothes__name', 'donor__username']
    list_filter = ['donation_date']
