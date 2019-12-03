from django.shortcuts import render
from .models import Squirrels




# Create your views here.

def sightings(request):
    sightings = Squirrels.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'Squirrel_Sightings/sightings.html', context)

def coordinates(request):
    sightings  = Squirrels.objects.all()[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, 'Squirrel_Sightings/map.html', context)
