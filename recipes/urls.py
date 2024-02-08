from django.contrib import admin
from django.urls import path
from . import views

app_name = "recipe"

urlpatterns = [
    path('', views.home, name="list"),
    path('recipes/<int:id>/', views.recipe, name="read"),
    path('recipes/category/<int:id>/', views.category, name="category"),
]