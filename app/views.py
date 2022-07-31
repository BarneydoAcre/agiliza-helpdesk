from django.shortcuts import render, HttpResponse
import json

def home(request):
    d = []

    return HttpResponse(json.dumps(d), status=200, headers={'content-type': 'application/json'})