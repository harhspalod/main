# forms.py in the 'wardrobe' app
from django import forms
from .models import Clothes

class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'image', 'category', 'is_old']
