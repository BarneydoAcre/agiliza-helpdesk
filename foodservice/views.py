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
        if body["type"] == 1:
            form = forms.AddProductForm(body)
            if form.is_valid():
                form.save()
                return HttpResponse(status=200, headers={'content-type': 'application/json'})
            return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
        elif body["type"] == 2:
            form = forms.AddProductSaleForm(body)
            if form.is_valid():
                last_id = form.save()
                return HttpResponse(last_id.id, status=200, headers={'content-type': 'application/json'})
            return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

def getProduct(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token'][0]) == 200:
            model = models.Product.objects.filter(company=get['company'][0], type=get['type'][0])
            data = []
            for m in model:
                if get['type'][0] == '2':
                    cost = getProductCost(m.id, get['company'][0])
                else: 
                    cost = m.cost
                data.append({
                    'id': str(m.id),
                    'name': str(m.name),
                    'brand': str(m.brand),
                    'measure': str(m.measure),
                    'stock': str(m.stock),
                    'cost': str(round(cost,2)),
                    'price': str(m.price),
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access Unautorized", status=402, headers={'content-type': 'application/json'})

def getProductCost(id, company):
    model = models.ProductItems.objects.filter(company=company, product=id)
    data = []
    cost = 0
    quantity = 0

    for m in model:
        cost += m.product_item.cost*m.quantity
        quantity += m.quantity

        data.append({
            'id': str(m.id),
            'cost': str(m.product_item.cost),
        })
    if quantity == 0:
        return 0
    else:    
        return cost/quantity

@csrf_exempt
def addProductItems(request):
    if request.method == "POST":
        body = json.loads(request.body)
        for i in body["items"]:
            form = forms.AddProductItemsForm({
                "company": body["company"],
                "company_worker": body["company_worker"],
                "product": body["product_sale"],
                "product_item": i["id"],
                "quantity": i["quantity"],
            })
            if form.is_valid():
                form.save()
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
        # return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

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
def addSale(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddSaleForm(body)
        if form.is_valid():
            last_id = form.save()
            return HttpResponse(last_id.id, status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

@csrf_exempt
def addSaleItems(request):
    if request.method == "POST":
        body = json.loads(request.body)
        for i in body["products"]:
            model = models.ProductItems.objects.filter(company=body["company"],product=i["id"])
            for m in model:
                models.Product.objects.filter(company=body["company"],id=m.product_item.id).update(stock=round(m.product_item.stock-float(i["quantity"]),2))
            data = {
                "company": body["company"],
                "company_worker": body["company_worker"],
                "sale": body["sale"],
                "product": i["id"],
                "quantity": i["quantity"],
                "price": i["price"],
            }
            form = forms.AddSaleItemsForm(data)
            if form.is_valid():
                form.save()
            else:
                return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

@csrf_exempt
def addProductStock(request):
    if request.method == "POST":
        body = json.loads(request.body)
        model = models.Product.objects.filter(company=body["company"],id=body["product"])
        for m in model:
            mod = m.cost*m.stock
            front = float(body["quantity"])*float(body["cost"])
            base = m.stock+float(body["quantity"])
            if m.stock == 0:
                model.update(stock=body["quantity"],cost=body["cost"])
            else:
                model.update(stock=round(m.stock+float(body["quantity"]),2),cost=(mod+front)/base) 
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})
