from django.shortcuts import render, reverse
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_list_or_404
from roulette.models import Location 
from rest_framework.views import Response 
from . import forms

#always pass in request
def index(request):
    # template = loader.get_template('roulette/index.html')
    # context = {}
    # return HttpResponse(template.render(context,request))
    form = forms.Filter()
    
    # if request.method=='POST':
    #     form=forms.Filter(request.POST)
        
    #     if form.is_valid():
    #     # Do SOMETHING WITH IT  
    #         print("Validation Success")
    #         print("Rating: "+form.cleaned_data['rating'])
    #         print('Price: '+form.cleaned_data['price'])
    #         print("Radius: "+form.cleaned_data['radius'])
    
    # return render(request,'results/main.html',{'form':form})
    # template=loader.get(template('results/main.html'))
    return render(request,'roulette/index.html',{'form':form})
    
    # return render(request,'results/main.html',{'form':form})
    # template=loader.get(template('results/main.html'))


def process_loc(request): #stores new lat and long in models
    template = loader.get_template('roulette/index.html')
    context={}
    lat = float(request.GET.get('lat'))
    lon = float(request.GET.get('lon'))

    Location.objects.all().delete()
    location = Location() 
    location.latitude = lat
    location.longitude = lon
    location.save()
    print(Location.objects.all())
    return HttpResponse(template.render(context,request))

def reload(request):
    template=loader.get_template('roulette/check.html')
    context={}
    return HttpResponseRedirect('/asdf/')

def asdf(request):
    form = forms.Filter()
    
    # return render(request,'results/main.html',{'form':form})
    # template=loader.get(template('results/main.html'))
    return render(request,'roulette/index.html',{'form':form})

def spinWheel(request):
    template = loader.get_template('results/main.html')
    context = {}
    return HttpResponseRedirect('/results/')

def goToResults(request):
    template = loader.get_template('results/main.html')
    context = {}
    # process_loc(request)
    # return HttpResponseRedirect(reverse('results:index'))
    return HttpResponseRedirect('/results/')

def form_page(request):
    form = forms.Filter()
    
    # return render(request,'results/main.html',{'form':form})
    # template=loader.get(template('results/main.html'))
    return render(request,'results/main.html',{'form':form})