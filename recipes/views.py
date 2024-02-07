from django.shortcuts import render

def home (request):
    return render(request=request, template_name='recipes/pages/home.html', context={
        'name': "Patrick Ferreira"
    })

def recipe(request, id):
    return render(request=request, template_name='recipes/pages/home.html', context={
        'name': 'Patrick Ferrera'
    })