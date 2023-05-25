from django.http import HttpResponse
from django.shortcuts import render

data = {
        'ziomki': [
            {
                'imie': 'klakson',
                'klata': 120,
                'przysiad': 90
            },
            {
                'imie': 'klarnet',
                'klata': 90,
                'przysiad': 20
            },
            {
                'imie': 'karton',
                'klata': 30,
                'przysiad': 180
            },
            {
                'imie': 'kefir',
                'klata': 360,
                'przysiad': 419
            }
        ]
}

def nauka(request):
    return render(request, 'nauka/nauka.html', data)

def home(request):
    return HttpResponse("Strona główna")