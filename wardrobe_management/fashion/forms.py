# forms.py in 'fashion' app
from django import forms
from .models import FashionBlog

class FashionBlogForm(forms.ModelForm):
    class Meta:
        model = FashionBlog
        fields = ['title', 'description', 'image']
