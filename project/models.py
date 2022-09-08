from django.db import models
from django.contrib.auth.models import User

import default.models
import suport.models

class Project(models.Model):
    company = models.ForeignKey(default.models.Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(default.models.CompanyWorker, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=False)
    customer_company = models.ForeignKey(suport.models.CustomerCompany, on_delete=models.PROTECT)
    customer_company_worker = models.ForeignKey(suport.models.CustomerCompanyWorker, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self

    class Meta:
        verbose_name, verbose_name_plural = "Project", "Projects"
        ordering = ("company",)
        
class ProjectStep(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    step = models.CharField(max_length=255, blank=False)
    finished = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self

    class Meta:
        verbose_name, verbose_name_plural = "Project", "Projects"
        ordering = ("company",)
        
