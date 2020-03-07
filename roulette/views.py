from django.shortcuts import render, reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_list_or_404
from roulette.models import Location 
from rest_framework.views import Response 

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
    location = Location(latitude = lat, longitude = lon) 
    location.save()
    print(Location.objects.all())
    return HttpResponse(template.render(context,request))

def reload(request):
    template=loader.get_template('roulette/check.html')
    context={}
    return HttpResponseRedirect('/asdf/')

def asdf(request):
    response = HttpResponse(); 
    return HttpResponseRedirect('/thank-you/')

def testprint():
    test = Location

def goToResults(request):
    template = loader.get_template('results/main.html')
    context = {}
    # return HttpResponseRedirect(reverse('results:index'))
    return HttpResponseRedirect('/results/')
