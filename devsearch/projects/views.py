from django.shortcuts import render
from django.http import HttpResponse

def recipes(request):
    return render(request, 'projects/recipes.html' )

def ingredients(request, pk):
    return render(request, 'projects/ingredients.html')

# Create your views here.
