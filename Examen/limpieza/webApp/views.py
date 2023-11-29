from django.shortcuts import render

def index(request):
    return render(request, 'webApp/index.html',{
        'title': 'Inicio'
    })

