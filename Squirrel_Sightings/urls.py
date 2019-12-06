from django.urls import path

from . import views

<<<<<<< HEAD
urlpatterns = [
=======
urlpatterns = [ 
>>>>>>> b2063779c1f4a19dc126db2bd0a489f79743795e
        path('',views.index),
        path('sightings/',views.sightings),
        path('map/',views.coordinates),
<<<<<<< HEAD
        path('<str:Unique_Squirrel_Id>/', views.edit_squirrel),
=======
        path('<str:Unique_Squirrel_Id>/edit/',views.edit_squirrel),
>>>>>>> 24cfea878f2404de42106825a0bde96780e68154
]
