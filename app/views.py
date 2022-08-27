from django.shortcuts import render, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import forms
import json
import requests as r

@csrf_exempt
def login(request):
    try:
        body = json.loads(request.body)
        email = body['email']
        password = body['password']
    except MultiValueDictKeyError:
        return HttpResponse("Do not have permission!", status=401, headers={'content-type': 'application/json'})
    
    User = models.User.objects.get(email=email)
    req = r.post('http://127.0.0.1:8000/auth/jwt/create/', {
        'username': User.username,
        'password': password
    })
    data = {
        'login_token': req.json(),
        'user_id': User.id,
        'username': User.username,
        'email': User.email
    } 

    return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})

def verifyLogin(token):
    req = r.post('http://127.0.0.1:8000/auth/jwt/verify/', {
        'token': token,
    })
    return req.status_code

def getCompany(request):
    try:
        email = request.GET['email']
    except MultiValueDictKeyError:
        return HttpResponse("Cannot find your email!", status=401, headers={'content-type': 'application/json'})
    try:
        key = request.GET['key']
    except MultiValueDictKeyError:
        return HttpResponse("Cannot find your key!", status=401, headers={'content-type': 'application/json'})

    if key == '8168':
        user = models.User.objects.get(email=email)
        companyworker = models.CompanyWorker.objects.filter(person=user).order_by('company')
        comp = []
        for w in companyworker:
            comp.append({
                'company_id': str(w.company.id),
                'company': str(w.company.company),
                'slug': str(w.company.slug),
                'email': str(w.person.email),
                'first_name': str(w.person.first_name), 
                'last_login': str(w.person.last_login)
            })
        return HttpResponse(json.dumps(comp), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Cannot find your key!", status=401, headers={'content-type': 'application/json'})

def getCustomerCompanys(request):
    try:
        get = request.GET
        token = get['token']
        company = get['company']
    except MultiValueDictKeyError:
        return HttpResponse("Do not have permission!", status=401, headers={'content-type': 'application/json'})
    
    if verifyLogin(token) == 200:
        companys = models.CustomerCompany.objects.filter(company=company)
        comp = []
        for c in companys:
            comp.append({
                'corporate_id': c.id,
                'corporate_name': c.corporate_name,
            })
        return HttpResponse(json.dumps(comp), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Invalid Token", status=401, headers={'content-type': 'application/json'})
        
def getCustomerCompanyWorkers(request):
    try:
        get = request.GET
        token = get['token']
        corporate = get['corporate']
        company = get['company']
    except MultiValueDictKeyError:
        return HttpResponse("Do not have permission!", status=401, headers={'content-type': 'application/json'})
    
    if verifyLogin(token) == 200:
        companyworkers = models.CustomerCompanyWorker.objects.filter(id=corporate)
        comp = []
        for cw in companyworkers:
            comp.append({
                'customer_id': cw.id,
                'customer_name': cw.customer_name,
            })
        return HttpResponse(json.dumps(comp), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Invalid Token", status=401, headers={'content-type': 'application/json'})

def getRequestTypes(request):
    try:
        get = request.GET
        token = get['token']
        company = get['company']
    except MultiValueDictKeyError:
        return HttpResponse("Do not have permission!", status=401, headers={'content-type': 'application/json'})
    
    if verifyLogin(token) == 200:
        companyworkers = models.RequestType.objects.filter(company=company)
        comp = []
        for cw in companyworkers:
            comp.append({
                'type_id': cw.id,
                'type_name': cw.request_name,
            })
        return HttpResponse(json.dumps(comp), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Invalid Token", status=401, headers={'content-type': 'application/json'})

def getTicket(request):
    try:
        get = request.GET
        token = get['token']
        company = get['company']
    except MultiValueDictKeyError:
        return HttpResponse("Do not have permission!", status=401, headers={'content-type': 'application/json'})
    
    if verifyLogin(token) == 200:
        tickets = models.Ticket.objects.filter(company=company).order_by('id')
        tick = []
        for t in tickets:
            tick.append({
                'id': t.id,
                'company': t.company.company,
                'company_worker_id': t.company_worker.id,
                'company_worker': t.company_worker.person.username,
                'title': t.title,
                'corporate_id': t.corporate.id,
                'corporate': t.corporate.corporate_name,
                'customer_id': t.customer.id,
                'customer': t.customer.customer_name,
                'type_id': t.type.id,
                'type': t.type.request_name,
                'routine': t.routine,
                'duty': t.duty,
                'description_problem': t.description_problem,
            })
        return HttpResponse(json.dumps(tick), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Invalid Token", status=401, headers={'content-type': 'application/json'})
        
def getTicketComments(request):
    try:
        get = request.GET
        token = get['token']
        company = get['company']
        ticket = get['ticket']
    except MultiValueDictKeyError:
        return HttpResponse("Do not have permission!", status=401, headers={'content-type': 'application/json'})
    
    if verifyLogin(token) == 200:
        tickets = models.TicketComment.objects.filter(ticket=ticket).order_by('id')
        tick = []
        for t in tickets:
            tick.append({
                'id': t.id,
                'ticket': t.ticket.id,
                'comment': t.comment,
                'created': t.created.strftime('%H:%M'),
                'worker': t.worker_comment.person.username
            })
        return HttpResponse(json.dumps(tick), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Invalid Token", status=401, headers={'content-type': 'application/json'})
        
@csrf_exempt
def addTicket(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddTicketForm(body)
        print(form.is_valid())
        print(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

@csrf_exempt
def addTicketComment(request):
    print()
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddTicketCommentForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'}) 
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Método inválido!", status=200, headers={'content-type': 'application/json'}) 

@csrf_exempt
def deleteTicket(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.DeleteTicketForm(body)
        if form.is_valid():
            models.Ticket.objects.get(id=body['id'], company=body['company']).delete()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addCustomerCompany(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddCustomerCompanyForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addCustomerCompanyWorker(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddCustomerCompanyWorkerForm(body)
        if form.is_valid():
            form.save()
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
        # return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})