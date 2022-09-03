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

class BugReportAdmin(admin.ModelAdmin):
    list_display = ('company', 'company_worker', 'bug',)
admin.site.register(models.BugReport, BugReportAdmin)