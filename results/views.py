from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import Response, APIView
from django.shortcuts import get_list_or_404
import requests
import json
from django.http import JsonResponse
from roulette.models import Location
from results.models import Restauraunt

# delte this later
from roulette.forms import FormName

# TODO: NEED TO CREATE FORMS FOR FILTERS LATER
#always pass in request
# def index(request):
#     template = loader.get_template('results/main.html')
#     context = {}
    # testResp(request)

# def testResp(request):
#     print("a;sdoijf;aoweijawefj")
#     api_key = 'z6bg8nnIj9vEeahsr6FRLJg-EYpp8WjqPApHnwpaerAnhzsSVu38SzJbOgwEMVMaJTHhoiiXjhKz5xKuUqbWvfunUrjv_c8Pjt3rIk_ZNpxEmck5l1-lji-PUeFpXXYx'
#     headers = {'Authorization': 'Bearer %s' % api_key}
#     url = 'https://api.yelp.com/v3/businesses/search'

#     lat = Location.objects.get(pk=3)
#     print("QUERTY OF LOCATION DB" + "asdf")

#     params = {'term':'restraunts','latitude':str(lat),'longitude':'-118.11'}

#     req = requests.get(url, params=params, headers=headers)

#     parsed = json.loads(req.text)

#     businesses = parsed["businesses"]#json format
    
#     for item in businesses: 
#         print("ITEM IS "+str(item)+ "\n")
#         print("Restaurant Name: "+str(item['name'])+"\n")
#         print("Rating is: "+ str(item['rating'])+ "\n")

#     # return HttpResponseObject(businesses, safe=False)
#     return Response(businesses)


# results
class foodView(APIView):

    # return of everything in data base for restraunts
    def get(self, request):
        api_key = 'z6bg8nnIj9vEeahsr6FRLJg-EYpp8WjqPApHnwpaerAnhzsSVu38SzJbOgwEMVMaJTHhoiiXjhKz5xKuUqbWvfunUrjv_c8Pjt3rIk_ZNpxEmck5l1-lji-PUeFpXXYx'
        headers = {'Authorization': 'Bearer %s' % api_key}

        url = 'https://api.yelp.com/v3/businesses/search'

        # use location from latest entry, 
        # TODO: either update entries or need to connect databases to users
        L = Location.objects.latest('latitude')

        # get variables for lat and long from Location Database
        latitude, longitude = L.latitude, L.longitude 

        params = {'term':'restraunts','latitude':str(latitude),'longitude':str(longitude)}
        req = requests.get(url, params=params, headers=headers)
        parsed = json.loads(req.text)
        businesses = parsed["businesses"]#json format

        for item in businesses: 
            restauraunt = Restauraunt()
            name =      str(item['name'])
            rating =    str(item['rating'])
            phone_num = str(item['phone'])
            
            price = str(item["price"]) if 'price' in item  else "N/A"


            print(price + '\n')
            restauraunt.name = name
            restauraunt.rating = rating
            restauraunt.phone_num = phone_num
            restauraunt.price = price
            restauraunt.foreign = L

            restauraunt.save()

            # print("ITEM IS "+str(item)+ "\n")
            # print("Restaurant Name: "+name+"\n")
            # print("Rating is: "+ rating+ "\n")


        return Response(businesses)
    
    # read information or refresh restraunts 
    def post(self, request):
        pass


def test(request):
    form = FormName
    # return HttpResponse(template.render(context,request))

    if request.method=='POST':
        form = FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING WITH IT
            print("Validation Success")
            print("Name: "+form.cleaned_data['name'])
            print('Email: '+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request,'results/main.html',{'form':form})
