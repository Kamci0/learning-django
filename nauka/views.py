from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Ziomki

def nauka(request):
    data = Ziomki.objects.all
    return render(request, 'nauka/nauka.html', {'ziomki': data})

def home(request):
    return HttpResponse("Strona główna")

def staty(request, id):
    data = Ziomki.objects.get(pk=id)
    return render(request, 'nauka/staty.html', {'ziomek': data})

def add(request):
    imie = request.POST.get('imie')
    klata = request.POST.get('klata')
    przysiad = request.POST.get('przysiad')

    if imie and klata and przysiad:
        ziomek = Ziomki(imie=imie, klata=klata, przysiad=przysiad)
        ziomek.save()
        return HttpResponseRedirect('/nauka')

    return render(request, 'nauka/add.html')

def delete(request, id):
    try:
        ziomek = Ziomki.objects.get(pk=id)
    except:
        raise Http404('Nie ma takiego kolegi')
    ziomek.delete()
    return HttpResponseRedirect('/nauka')
