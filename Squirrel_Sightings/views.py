from django.http import HttpResponse
import random

def index(request):
    i = random.random()
    return HttpResponse(f"Welcome!{i}")

# Create your views here.
