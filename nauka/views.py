from django.http import HttpResponse
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
