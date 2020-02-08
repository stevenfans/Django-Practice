from django.shortcuts import render, reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_list_or_404
from roulette.models import Location 


# from rest_framework.views import APIView
# from rest_framework import status

# Create your views here.

#always pass in request
def index(request):
    template = loader.get_template('roulette/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def process_loc(request):
    template = loader.get_template('roulette/index.html')
    context={}
    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))
    print('latitdue is', lat)
    print('longitude is', lon)
    #location = Location(latitude = lat, longitude = lon) 
    #location.save()
    #print(Location.objects.all())
    return HttpResponse(template.render(context,request))

def testprint():
    test = Location

def goToResults(request):
    print("test")
    template = loader.get_template('results/main.html')
    context = {}
    # return HttpResponseRedirect(reverse('results:index'))
    return HttpResponseRedirect('/results')
