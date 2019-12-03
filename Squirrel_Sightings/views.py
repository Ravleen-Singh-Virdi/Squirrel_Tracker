from django.http import HttpResponse
import random
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels

def index(request):
    context = {"Squirrel Sightings": Squirrels.objects.all(), "field_names": Squirrels._meta.get_fields()}
    return render(request, 'Squirrel_Sightings/index.html',context)

# Create your views here.
