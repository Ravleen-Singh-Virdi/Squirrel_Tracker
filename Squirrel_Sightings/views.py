from django.http import HttpResponse
import random
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels

def index(request):
    context = {"Squirrel Sightings": Squirrels.objects.all(), "field_names": Squirrels._meta.get_fields()}
    return render(request, 'Squirrel_Sightings/index.html',context)

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
