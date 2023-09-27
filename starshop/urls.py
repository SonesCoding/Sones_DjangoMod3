
from django.urls import path 
from . import views
urlpatterns = [

    path('', views.hp , name='hp'),
    path('bye/<int:pk>/', views.bye, name='bye'), #added the pk field so you can grab the specific star
    path('basic', views.basic, name='basic'),
]
