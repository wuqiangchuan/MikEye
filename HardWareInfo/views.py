from django.shortcuts import render
from django.template.context_processors import request
from django.http.request import HttpRequest

# Create your views here.
import json
from django.http.response import HttpResponse
#def Client(request):
#    pass

def TestFunc(request):
    if request.method == 'POST':
        ReceviedData = json.loads(request.body)
        print ReceviedData
        
        #return HttpResponse(json.dumps(ReceviedData)) 
        return HttpResponse('ok') 
    