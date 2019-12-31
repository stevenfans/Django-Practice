from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#always pass in request
def index(request):
    template = loader.get_template('roulette/index.html')
    context = {
        
    }
   #return HttpResponse("<h1>This is the page for the roullete main page</h1>")
    return HttpResponse(template.render(context,request))