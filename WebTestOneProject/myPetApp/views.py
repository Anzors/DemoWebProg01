from django.shortcuts import render
from django.http import Http404 

from .models import Pet

def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404("Pet does not exist")
    return render(request, 'pet_detail.html', {'pet':pet,})

def home(request):
    pets = Pet.objects.all()
    return render(request, "home.html", {"pets":pets,})


