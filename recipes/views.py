from django.shortcuts import render
from utils.recipes.factory import make_recipe
from django.http import Http404

from .models import Recipe

def home (request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request=request, template_name='recipes/pages/home.html', context={
        'recipes': recipes,
    })

def category (request, id):
    recipes = Recipe.objects.filter(category__id=id, is_published=True).order_by('-id')

    if not recipes:
        raise Http404('Not Found :(')

    return render(request=request, template_name='recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name}  - Category |'
    })

def recipe (request, id):
    return render(request=request, template_name='recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })