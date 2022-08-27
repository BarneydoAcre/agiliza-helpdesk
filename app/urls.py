from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('auth/login/', views.login),
    path('getCompany/', views.getCompany),
    path('getCustomerCompanys/', views.getCustomerCompanys),
    path('addCustomerCompany/', views.addCustomerCompany),
    path('addCustomerCompanyWorker/', views.addCustomerCompanyWorker),
    path('getCustomerCompanyWorkers/', views.getCustomerCompanyWorkers),
    path('getRequestTypes/', views.getRequestTypes),
    path('addTicket/', views.addTicket),
    path('getTicket/', views.getTicket),
    path('addTicketComment/', views.addTicketComment),
    path('getTicketComments/', views.getTicketComments),
    path('deleteTicket/', views.deleteTicket),
    path('auth/', include('djoser.urls.jwt')),
]