## Steps to start s project

-  django-admin startproject devsearch
-  python manage.py runserver 
-  dev search is the website 
-  a project is made up of multiple apps 
- 

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