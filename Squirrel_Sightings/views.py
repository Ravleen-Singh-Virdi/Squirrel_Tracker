from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels
from .forms import SquirrelForm

def index(request):
    context = {
            "sightings":Squirrels.objects.all(),"field_names":Squirrels._meta.get_fields()
        }
    return render(request, 'Squirrel_Sightings/index.html',context)

def sightings(request):
    squirrels = Squirrels.objects.all()
    context = {
            "squirrels": squirrels,
        }
    return render(request, 'Squirrel_Sightings/sightings.html', context)

def coordinates(request):
    squirrels  = Squirrels.objects.all()[:100]
    context = {
            "squirrels": squirrels,
         }
    return render(request, 'Squirrel_Sightings/map.html', context)

def edit_squirrel(request, Unique_Squirrel_Id):
    squirrel = Squirrels.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        #check the form data
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel_Sightings/{Unique_Squirrel_Id}')
    else:
        form = SquirrelForm(instance=squirrel)
    context = {
            'form':form,
        }
    return render(request, 'Squirrel_Sightings/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        #check the form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/Squirrel_Sightings/list/')
    else:
        form = SquirrelForm()
    context = {
            'form':form,
        }
    return render(request, '/Squirrel_Sightings/edit.html', context)

def stats(request):
    black_count = 0
    cinnamon_count = 0
    gray_count = 0
    eating_count = 0
    juvenile_count = 0
    adult_count = 0
    running_count=0
    climbing_count
    chasing_count = 0
    foraging_count = 0
    kuks_count = 0
    quaas_count = 0
    moans_count = 0
    tail_flags_count=0
    for s in Squirrels.objects.all():
        if s.Running == True:
             running_count +=1
        else:
             pass
        if s.Climbing == True:
             climbing_count +=1
        else:
             pass
        if s.Chasing == True:
             chasing_count +=1
        else:
             pass
        if s.Primary_Fur_Color == 'Black':
            black_count +=1
        elif s.Primary_Fur_Color == 'Cinnamon':
            cinnamon_count +=1
        elif s.Primary_Fur_Color == 'Gray':
            gray_count +=1
        else:
            pass
        if s.Foraging == True:
             foraging_count +=1
        else:
             pass
        if s.Eating == True:
             eating_count +=1
        else:
             pass
        if s.Age == 'Juvenile':
            juvenile_count +=1
        elif s.Age == 'Adult':
            adult_count +=1
        else:
            pass
        if s.Kuks == True:
            kuks_count +=1
        else:
            pass
        if s.Quaas ==True:
            quaas_count +=1
        else:
            pass
        if s.Moans == True:
            moans_count +=1
        else:
            pass
        if s.Tail_Flags == True:
             tail_flags_count +=1
        else:
             pass

    context = {'Eating:': eating_count,
                'Running':running_count,
                'Climbing':climbing_count,
                'Chasing':chasing_count,
                'Black Fur':black_count,
                'Cinnamon Fur':cinnamon_count,
                'Gray Fur':gray_count,
                'Foraging':foraging_count,
                'Flagging tails':tail_flags_count,
                'Juvenile':juvenile_count,
                'Adult': adult_count,
                'Kuks':kuks_count,
                'Quaas':quaas_count,
                'Moans': moans_count,
            }
    return render(request, 'Squirrel_Sightings/stats.html', context)

