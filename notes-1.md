## Steps to start s project

-  django-admin startproject devsearch
-  python manage.py runserver 
-  dev search is the website 
-  a project is made up of multiple apps 


## create an app
- python manage.py startapp projects 
- register app with SETTINGS project in devsearch


## URLS and Views
- devsearch/urls.py - url routing  path for the entire project 
- every route we go to, we return a function 
- 
```yaml
## here is how it works 
www.facebook.com/about
paths = [/home, /about]
returns

about.html

## projects get big and views should not be in the urls

- projects app will manage the views 
- create a new file called urls.py in your app as well
```

## MAKE Django know about the app urls 
- use include function
- path('', include('projects.urls'))
- 

## templates and views
- in project dir(manage.py dir), not the app dir, create templates foldser
- create templates on recipes and ingredients 
- - let django find this template
- settings.py 
- import os - yo set file path
- Go to TEMPLATES variable in DIRS 
- os.path.join(BASE_DIR, 'templates'),
- 

## render with view 

`def recipes(request):
    return render(request, 'recipes.html' )`

## template inheritance
```python
navbar.html

include the functionality of navbar.html to other templates using jinja 

{% include 'navbar.html' %}
```
## main.html
- style this page and use to format all the pages 
- - added navbar
- evey page that inherits from main will have navbar
- 
## child content of main.html

{% block content %}

{% endblock content  %}

## recipes

{% extends 'main.html' %}

{% block content %}
<h1></h1>
{% endblock content  %}


## seperate templates according django
- main and navbar will remain the same location
- anything with projecta wirh proiects app include templates 
- in projects app, create  templates, inisde templates create projects(app name).
- templates file will be in the projects folder 
- projects/recipes.html


## Rendering Data into templates 