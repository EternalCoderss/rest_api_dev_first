from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.


def students(request):

    data = {
        {   
           "id": 1,
           "name": "Shivam",
           "age" : 25

        }
    }
    # return HttpResponse(data, '<h3>Hello django api working!</h3>')

    return HttpResponse(
        json.dumps(data),
        content_type = "application/json"
    )