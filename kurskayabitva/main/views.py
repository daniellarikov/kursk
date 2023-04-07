from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render (request, 'main/main-page-total.html')

def tech(request):
    return render (request, 'main/ground.html')

def airplanes(request):
    return render (request, 'main/airplanes.html')

def fire_guns(request):
    return render (request, 'main/fire_guns.html')

def heroes(request):
    return render (request, 'main/heroes-page.html')

def history(request):
    return render (request, 'main/history-page.html')