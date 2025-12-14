from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """Main sheet"""
    return HttpResponse("<h1>Привет! Это главная страница!</h1>")


def about(request):
    """Main sheet"""
    return HttpResponse("<h1>Привет! Это страница о нас!</h1>")
