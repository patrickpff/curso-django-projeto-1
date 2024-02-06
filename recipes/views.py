from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request=request, template_name='recipes/home.html', context={
        'name': "Patrick"
    })

def contact(request):
    return HttpResponse("HELLO WORLD - CONTATO")

def about(request):
    return HttpResponse("HELLO WORLD - SOBRE")