# models.py in the 'wardrobe' app
from django.db import models

class Clothes(models.Model):
    CATEGORY_CHOICES = [
        ('T-shirt', 'T-shirt'),
        ('Jeans', 'Jeans'),
        ('Jacket', 'Jacket'),
        # Add more categories as needed
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clothes_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_old = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
