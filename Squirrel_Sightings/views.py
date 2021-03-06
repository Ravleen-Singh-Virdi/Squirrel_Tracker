from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels
from .forms import SquirrelForm

def landing(request):
    return render(request, 'Squirrel_Sightings/landing.html')

def view_all(request):
    context = {
            "sightings":Squirrels.objects.all(),"field_names":Squirrels._meta.get_fields()
        }

    return render(request, 'Squirrel_Sightings/view_all.html',context)

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
            return redirect(f'/squirrel_sightings/view/')
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
            return redirect(f'/squirrel_sightings/')
    else:
        form = SquirrelForm()
    context = {
            'form':form,
        }
    return render(request, 'Squirrel_Sightings/add.html', context)

def stats(request):
    black_count = 0
    cinnamon_count = 0
    gray_count = 0
    eating_count = 0
    juvenile_count = 0
    adult_count = 0
    running_count=0
    climbing_count = 0
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
        if s.Quaas == True:
            quaas_count +=1
        else:
            pass
        if s.Moans == True:
            moans_count +=1
        else:
            pass
        if s.Tail_flags == True:
             tail_flags_count +=1
        else:
             pass

    details = {'Number of squirrels found eating': eating_count,
                'Number of squirrels found running':running_count,
                'Number of squirrels found climbing':climbing_count,
                'Number of squirrels found chasing':chasing_count,
                'Number of squirrels found with black fur':black_count,
                'Number of squirrels found with cinnamon fur':cinnamon_count,
                'Number of squirrels found with gray fur':gray_count,
                'Number of squirrels found foraging':foraging_count,
                'Number of squirrels found flagging tails':tail_flags_count,
                'Number of squirrels found as a juvenile':juvenile_count,
                'Number of squirrels found as a adult': adult_count,
                'Number of squirrels found making kuk sounds':kuks_count,
                'Number of squirrels found making quaas sounds':quaas_count,
                'Number of squirrels found making moan sounds': moans_count,
            }
    context = {"stats":details}
    return render(request, 'Squirrel_Sightings/stats.html', context)

