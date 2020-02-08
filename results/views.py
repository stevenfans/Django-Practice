from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

#always pass in request
def index(request):
    template = loader.get_template('results/main.html')
    context = {}
    return HttpResponse('<h1>TEST</h1>4')
    # return HttpResponse(template.render(context, request)); 
