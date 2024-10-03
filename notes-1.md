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


## render with view 

`def recipes(request):
    return render(request, 'recipes.html' )`

## template inheritance
```python
navbar.html

include the functionality of navbar.html to other templates using django templating engine jinja 

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
- first just make the project page our default 
-  make the url and empty string ''
```python
## example of using jinja 

My first name is {{ first_name }} My last name is {{ lsat_name }}

## access object in the template

{{ my_dict.key }}

{{ my_object.attribute }}

{{ my_list.0 }}

## using tags for conditions 

{% if user.is_authenticated %}Hello, {{ user.username}}.{% endif %}

## accesing variables from views ,py
msg = "This is the view page"

- pass it as dict 
- return render(request, 'projects/recipes.html, {'msg': msg})
- access the key in the template

## writing the dict gets bigger, have a variable called context
def recipes(request):
    msg = 'main project'
    return render(request, 'projects/recipes.html', context)

## writing an if statememtt is using a single curly brace

## output dictionary by pasting the dictionary in the views.py
- and output it on the template reccipes.html

<ul>
    {% for project in projects  %}
    <li>Title:{{project.title}}</li>
    {% endfor  %}

<ul>

## dynamic page rendering using the url name 
 <li>Title:<a href= "{% url 'recipe' projects.id %}">{{project.title}}
</li>
```
## Building our database