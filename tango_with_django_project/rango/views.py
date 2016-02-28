from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Rango says hello there! <br/> Here is the about page-<a href='/rango/about'>About</a>")
def about(request):
    return HttpResponse("Rango is now displaying the about page! <br/> Here is the main page-<a href='/rango/'>Index</a>")