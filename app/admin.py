from django.contrib import admin
from . import models


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'owner')
admin.site.register(models.Company, CompanyAdmin)

class CompanyWorkerAdmin(admin.ModelAdmin):
    list_display = ('person', 'company', 'cpf', 'position')
admin.site.register(models.CompanyWorker)

class CompanyPositionAdmin(admin.ModelAdmin):
    list_display = ('position',)
admin.site.register(models.CompanyPosition, CompanyPositionAdmin)

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'person')
admin.site.register(models.PaymentMethod, PaymentMethodAdmin)

class RequestTypeAdmin(admin.ModelAdmin):
    list_display = ('company', 'request_name',)
admin.site.register(models.RequestType, RequestTypeAdmin)

class CustomerCompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'corporate_name', 'corporate_cnpj',)
admin.site.register(models.CustomerCompany, CustomerCompanyAdmin)

class CustomerCompanyWorkerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'corporate',)
admin.site.register(models.CustomerCompanyWorker, CustomerCompanyWorkerAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'company_worker', 'customer')
admin.site.register(models.Ticket, TicketAdmin)

class TicketStatusAdmin(admin.ModelAdmin):
    list_display = ('company', 'status')
admin.site.register(models.TicketStatus, TicketStatusAdmin)

class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'comment',)
admin.site.register(models.TicketComment, TicketCommentAdmin)
