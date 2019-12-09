from django.urls import path

from . import views

urlpatterns = [ 
        path('view/',views.view_all),
        path('',views.landing),
        path('stats/',views.stats),
        path('add/', views.add_squirrel),
        path('map/',views.coordinates),
        path('view/<str:Unique_Squirrel_Id>/edit/',views.edit_squirrel),
]
