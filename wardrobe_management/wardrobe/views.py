# views.py in the 'wardrobe' app
from django.shortcuts import render, redirect
from .models import Clothes
from .forms import ClothesForm

def home(request):
    clothes = Clothes.objects.all()
    return render(request, 'wardrobe/home.html', {'clothes': clothes})

def add_clothes(request):
    if request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClothesForm()
    return render(request, 'wardrobe/add_clothes.html', {'form': form})

def update_clothes(request, id):
    cloth = Clothes.objects.get(id=id)
    if request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES, instance=cloth)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClothesForm(instance=cloth)
    return render(request, 'wardrobe/update_clothes.html', {'form': form})

def delete_clothes(request, id):
    cloth = Clothes.objects.get(id=id)
    cloth.delete()
    return redirect('home')
