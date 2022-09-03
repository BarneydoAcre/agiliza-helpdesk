from django.shortcuts import render, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from . import forms
from . import models
import json

@csrf_exempt
def addBugReport(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddBugReportForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})