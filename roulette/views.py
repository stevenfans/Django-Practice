from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_list_or_404

# from rest_framework.views import APIView
# from rest_framework import status

# Create your views here.

#always pass in request
def index(request):
    template = loader.get_template('roulette/index.html')
    # lat = float(request.GET.get('lat'))
    context = {}
   #return HttpResponse("<h1>This is the page for the roullete main page</h1>")
    return HttpResponse(template.render(context,request))

def process_loc(request):
    template = loader.get_template('roulette/index.html')
    contex={}
    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))
    print('latitdue is', lat)
    print("FUCK ME, Why do you work????")
    return HttpResponse(template.render(context,request))
