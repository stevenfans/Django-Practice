from django.shortcuts import render, reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_list_or_404
from roulette.models import Location 
from rest_framework.views import Response 

# from rest_framework.views import APIView
# from rest_framework import status



# Create your views here.

# # results
# class foodView(APIView):

#     # return of everything in data base for restraunts
#     def get(self):
#         pass
    
#     # read information or refresh restraunts 
#     def post(self):
#         pass

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
    location = Location(latitude = lat, longitude = lon) 
    location.save()
    print(Location.objects.all())
    return HttpResponse(template.render(context,request))

def reload(request):
    print("asd;jfa;wjfe;oasidfaj;wejf;")
    template=loader.get_template('roulette/check.html')
    context={}
    # return redirect('http://127.0.0.1:8000/roulette/asdf')
    # return redirect('asdf')
    return HttpResponseRedirect('/asdf/')

def asdf(request):
    print("asdf");
    response = HttpResponse(); 
    # return HttpResponse("<h1>test</h1>")
    return HttpResponseRedirect('/thank-you/')

def testprint():
    test = Location

def goToResults(request):
    print("tasdfasdfafdest")
    template = loader.get_template('results/main.html')
    context = {}
    # return HttpResponseRedirect(reverse('results:index'))
    return HttpResponseRedirect('/results/')
