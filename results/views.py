from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#always pass in request
def index(request):
    return HttpResponse("<h1>This is the page for the results  page</h1>")
