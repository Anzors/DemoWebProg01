from django.shortcuts import render
from django.http import HttpResponse

from .models import Pet

def pet_detail(request, pet_id):
    return HttpResponse(F"<h1>Pet number: {pet_id}</h1>")

def home(request):
    pets = Pet.objects.all()
    return render(request, "home.html", {"pets":pets,})
