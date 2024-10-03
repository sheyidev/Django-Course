
from django.urls import path
from . import views




urlpatterns = [

    path('recipe/', views.recipes, name="recipe"),
    path('ingredient/<str:pk>', views.ingredients, name="ingredient"),
]
