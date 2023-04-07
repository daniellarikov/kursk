from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('inform_page', views.tech, name='ground'),
    path('airplanes', views.airplanes, name='airplanes'),
    path('fire_guns', views.fire_guns, name='fire_guns'),
    path('heroes', views.heroes, name = 'heroes'),
    path('history', views.history, name = 'history')
]