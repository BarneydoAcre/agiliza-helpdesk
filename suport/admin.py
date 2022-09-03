from django.contrib import admin

from . import models


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

