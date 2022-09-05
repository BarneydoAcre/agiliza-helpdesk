from django.shortcuts import render, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from default.views import verifyLogin
from . import models
from . import forms
import json
from datetime import datetime
import requests as r

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
        companyworkers = models.CustomerCompanyWorker.objects.filter(corporate_id=corporate)
        comp = []
        for cw in companyworkers:
            comp.append({
                'customer_id': cw.id,
                'customer_name': cw.customer_name,
            })
        return HttpResponse(json.dumps(comp), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Invalid Token", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addRequestType(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddRequestTypeForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

def getRequestType(request):
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

@csrf_exempt
def deleteRequestType(request):
    body = json.loads(request.body)
    # token = get['token']
    company = body['company']
    id = body['id']
    if request.method == "POST":
        models.RequestType.objects.filter(company=company, id=id).delete()
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=402, headers={'content-type': 'application/json'})

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
        worker = get['worker']
        date = get['date'].split(',')
        status = get['status']
    except MultiValueDictKeyError:
        return HttpResponse("Do not have permission!", status=401, headers={'content-type': 'application/json'})
    if verifyLogin(token) == 200:
        print(date)
        if (date == ['null']) and (status == 'null') and (worker == 'null'):
            tickets = models.Ticket.objects.filter(company=company).order_by('id')
        if (date != ['null']) and (status == 'null') and (worker =='null'):
            tickets = models.Ticket.objects.filter(company=company,created__range=(datetime.strptime(date[0], '%Y-%m-%d').date(), datetime.strptime(date[1], '%Y-%m-%d').date())).order_by('id')
        if (date == ['null']) and (status != 'null') and (worker =='null'):
            tickets = models.Ticket.objects.filter(company=company,status=status).order_by('id')
        if (date == ['null']) and (status == 'null') and (worker !='null'):
            tickets = models.Ticket.objects.filter(company=company,company_worker=worker).order_by('id')
        if (date != ['null']) and (status != 'null') and (worker =='null'):
            tickets = models.Ticket.objects.filter(company=company,status=status,created__range=(datetime.strptime(date[0], '%Y-%m-%d').date(), datetime.strptime(date[1], '%Y-%m-%d').date())).order_by('id')
        if (date == ['null']) and (status != 'null') and (worker !='null'):
            tickets = models.Ticket.objects.filter(company=company,status=status,company_worker=worker).order_by('id')
        if (date != ['null']) and (status == 'null') and (worker !='null'):
            tickets = models.Ticket.objects.filter(company=company,created__range=(datetime.strptime(date[0], '%Y-%m-%d').date(), datetime.strptime(date[1], '%Y-%m-%d').date()),company_worker=worker).order_by('id')
        if (date != ['null']) and (status != 'null') and (worker !='null'):
            tickets = models.Ticket.objects.filter(company=company,status=status,created__range=(datetime.strptime(date[0], '%Y-%m-%d').date(), datetime.strptime(date[1], '%Y-%m-%d').date()),company_worker=worker).order_by('id')
        tick = []
        for t in tickets:
            tick.append({
                'id': t.id,
                'title': t.title,
                'company_name': t.company.company,
                'company_worker_id': t.company_worker.id,
                'company_worker_name': t.company_worker.person.username,
                'corporate_id': t.corporate.id,
                'corporate_name': t.corporate.corporate_name,
                'customer_id': t.customer.id,
                'customer_name': t.customer.customer_name,
                'type_id': t.type.id,
                'type_name': t.type.request_name,
                'routine': t.routine,
                'duty': t.duty,
                'description_problem': t.description_problem,
                'status_id': t.status.id,
                'status_name': t.status.status,
            })
        return HttpResponse(json.dumps(tick), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Invalid Token", status=401, headers={'content-type': 'application/json'})


def getCompanyWorkers(request):
    try:
        get = request.GET
        token = get['token']
        company = get['company']
    except MultiValueDictKeyError:
        return HttpResponse("Do not have permission!", status=401, headers={'content-type': 'application/json'})

    if verifyLogin(token) == 200:
        status = models.CompanyWorker.objects.filter(company=company)
        stat  = []
        for s in status:
            stat.append({
                'worker_id': s.id,
                'worker_name': s.person.username,
            })
        return HttpResponse(json.dumps(stat), status=200, headers={'content-type': 'application/json'})
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
        print(body  )
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
        if len(models.TicketComment.objects.filter(ticket=body['id'])) != 0:
            return HttpResponse(status=401, headers={'content-type': 'application/json'})
        if form.is_valid():
            models.Ticket.objects.get(id=body['id'], company=body['company']).delete()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse(status=402, headers={'content-type': 'application/json'})
    return HttpResponse(status=403, headers={'content-type': 'application/json'})

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
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def closeTicket(request):
    if request.method == "POST":
        body = json.loads(request.body)
        models.Ticket.objects.filter(id=body['id']).update(status=2)
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addTicketStatus(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddTicketStatusForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def deleteTicketStatus(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.deleteTicketStatusForm(body)
        if form.is_valid():
            models.TicketStatus.objects.filter(id=body['id']).delete()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def updateTicketStatus(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.updateTicketStatusForm(body)
        if form.is_valid():
            models.Ticket.objects.filter(id=body['ticket'],company=body['company']).update(status=body['status_id'])
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})

def getTicketStatus(request):
    # if verifyLogin(token) == 200:
    if request.method == "GET":
        status = models.TicketStatus.objects.all()
        stat  = []
        for s in status:
            stat.append({
                'status_id': s.id,
                'status_name': s.status,
            })
        return HttpResponse(json.dumps(stat), status=200, headers={'content-type': 'application/json'})
    return HttpResponse("Invalid Token", status=401, headers={'content-type': 'application/json'})