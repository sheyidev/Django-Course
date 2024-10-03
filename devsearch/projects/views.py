from django.shortcuts import render
from django.http import HttpResponse

def recipes(request):
    return HttpResponse('Here is the recipes page')

def ingredients(reques, pk):
    return HttpResponse('Here is the INGREDIENT page' + ' ' + str(pk))

# Create your views here.
