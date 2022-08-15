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
