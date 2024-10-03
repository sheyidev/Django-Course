from django.shortcuts import render
from django.http import HttpResponse


projectsList = [

    {

        'id': '1',
        'title': "Ecommerce website",
        'description': 'fully functional ecommerce website'
    },
        {

        'id': '2',
        'title': "recipe",
        'description': 'A recipe page for users '
    },

        {

        'id': '3',
        'title': "Social Network",
        'description': 'Awesome open source project'
    },
]

def recipes(request):
    msg = 'main project'
    num = 12
    context = {'page': msg, 'num': num, 'projects':projectsList}

    return render(request, 'projects/recipes.html', context)
    #return render(request, 'projects/recipes.html', {'page': msg})

def ingredients(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/ingredients.html', {'projects': projectObj})

# Create your views here.
