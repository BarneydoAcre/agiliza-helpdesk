from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

from default.views import verifyLogin
from . import forms
from . import models
import json

@csrf_exempt
def addProduct(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddProductForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

def getProduct(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token']) == 200:
            data = []
            for m in models.Product.objects.filter(company=get['company'][0]):
                data.append({
                    'id': str(m.id),
                    'name': str(m.name),
                    'brand': str(m.brand),
                    'measure': str(m.measure),
                    'stock': str(m.stock),
                    'cost': str(m.cost),
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse(status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addBrand(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddBrandForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

def getBrand(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token']) == 200:
            data = []
            for m in models.ProductBrand.objects.filter(company=get['company'][0]):
                data.append({
                    'brand_id': m.id,
                    'brand_name': m.brand,
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse(status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addMeasure(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddMeasureForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

def getMeasure(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token']) == 200:
            data = []
            for m in models.ProductMeasure.objects.filter(company=get['company'][0]):
                data.append({
                    'measure_id': m.id,
                    'measure_name': m.measure,
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse(status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addProductSale(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddProductSaleForm(body)
        print(form.is_valid())
        if form.is_valid():
            last_id = form.save()
            print(last_id.id)
            return HttpResponse(last_id.id, status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

def getProductSale(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token']) == 200:
            data = []
            for m in models.ProductSale.objects.filter(company=get['company'][0]):
                data.append({
                    'id': m.id,
                    'name': m.name,
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse(status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addProductSaleItems(request):
    if request.method == "POST":
        body = json.loads(request.body)
        for i in body["items"]:
            form = forms.AddProductSaleItemsForm({
                "company": body["company"],
                "company_worker": body["company_worker"],
                "product_sale": body["product_sale"],
                "product": i["id"]
            })
            if form.is_valid():
                form.save()
                return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})
