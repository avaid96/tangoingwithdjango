from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    #return HttpResponse("Rango says hello there! <br/> Here is the about page-<a href='/rango/about'>About</a>")
    context_dict={'boldmessage':"I am bold font from the context"}
    return render(request, 'rango\index.html', context_dict)
def about(request):
    return HttpResponse("Rango is now displaying the about page! <br/> Here is the main page-<a href='/rango/'>Index</a>")