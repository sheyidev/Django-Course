
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    ## '' - this is the domain
    path('', include('projects.urls'))
]
