from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import Response, APIView
from django.shortcuts import get_list_or_404

import requests
import json
from django.http import JsonResponse


# Create your views here.

#always pass in request
def index(request):
    template = loader.get_template('results/main.html')
    context = {}
    # return HttpResponse('<h1>TEST</h1>4')
    # return HttpResponse(template.render(context, request)); 
    testResp(request)

def testResp(request):
    api_key = 'z6bg8nnIj9vEeahsr6FRLJg-EYpp8WjqPApHnwpaerAnhzsSVu38SzJbOgwEMVMaJTHhoiiXjhKz5xKuUqbWvfunUrjv_c8Pjt3rIk_ZNpxEmck5l1-lji-PUeFpXXYx'
    headers = {'Authorization': 'Bearer %s' % api_key}

    url = 'https://api.yelp.com/v3/businesses/search'
    params = {'term':'restraunts','latitude':'33.78','longitude':'-118.11'}

    req = requests.get(url, params=params, headers=headers)

    parsed = json.loads(req.text)

    businesses = parsed["businesses"]#json format
    
    for item in businesses: 
        print("ITEM IS "+str(item)+ "\n")
        print("Restaurant Name: "+str(item['name'])+"\n")
        print("Rating is: "+ str(item['rating'])+ "\n")

    # return HttpResponseObject(businesses, safe=False)
    return Response(businesses)


# results
class foodView(APIView):

    # return of everything in data base for restraunts
    def get(self, request):
        api_key = 'z6bg8nnIj9vEeahsr6FRLJg-EYpp8WjqPApHnwpaerAnhzsSVu38SzJbOgwEMVMaJTHhoiiXjhKz5xKuUqbWvfunUrjv_c8Pjt3rIk_ZNpxEmck5l1-lji-PUeFpXXYx'
        headers = {'Authorization': 'Bearer %s' % api_key}

        url = 'https://api.yelp.com/v3/businesses/search'
        params = {'term':'restraunts','latitude':'33.78','longitude':'-118.11'}

        req = requests.get(url, params=params, headers=headers)

        parsed = json.loads(req.text)

        businesses = parsed["businesses"]#json format
        
        for item in businesses: 
            print("ITEM IS "+str(item)+ "\n")
            print("Restaurant Name: "+str(item['name'])+"\n")
            print("Rating is: "+ str(item['rating'])+ "\n")

        # return HttpResponseObject(businesses, safe=False)
        return Response(businesses)
    
    # read information or refresh restraunts 
    def post(self, request):
        pass