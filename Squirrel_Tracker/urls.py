"""Squirrel_Tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
<<<<<<< HEAD
    path('squirrel_sightings/',include('Squirrel_Sightings.urls')),
=======
    path('squirrel_sightings/', include('Squirrel_Sightings.urls')),   
>>>>>>> 4878417dc9c0c79d150b1703348f3d36e6b9b8b0
    path('admin/', admin.site.urls),
]
