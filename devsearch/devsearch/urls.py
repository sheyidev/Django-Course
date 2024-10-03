
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def recipes(request):
    return HttpResponse('Here is the recipes page')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', recipes, name="recipe"),
]
