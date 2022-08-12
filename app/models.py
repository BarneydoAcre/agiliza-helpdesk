from django.db import models
from django.contrib.auth.models import User

class UserProxy(User):   
    class Meta:
        proxy = True

class Company(models.Model):
    owner = models.ForeignKey("UserProxy", on_delete=models.PROTECT)
    slug = models.CharField(max_length=255, blank=False)
    company = models.CharField(max_length=255, blank=False)
    cnpj = models.IntegerField(blank=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.company)

    class Meta:
        verbose_name, verbose_name_plural = "Company", "Companys"
        ordering = ("company",)

class CompanyWorker(models.Model):
    person = models.ForeignKey("UserProxy", on_delete=models.PROTECT)
    company = models.ForeignKey("Company", on_delete=models.PROTECT)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    phone_number = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.person)
    
    class Meta:
        verbose_name, verbose_name_plural = "Company Worker", "Company Workers"
        ordering = ("person",)

class CompanyPosition(models.Model):
    company = models.ForeignKey("Company", on_delete=models.PROTECT)
    position = models.CharField(max_length=25, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.position)

    class Meta:
        verbose_name, verbose_name_plural = "Company Position", "Company Positions"
        ordering = ("position",)

class CompanyWorkerPosition(models.Model):
    company = models.ForeignKey("Company", on_delete=models.PROTECT)
    companyWorker = models.ForeignKey("CompanyWorker", on_delete=models.PROTECT)
    position = models.ForeignKey("CompanyPosition", on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.position)

    class Meta:
        verbose_name, verbose_name_plural = "Company Worker Position", "Company Worker Positions"
        ordering = ("companyWorker",)

class PaymentMethod(models.Model):
    person = models.ForeignKey("UserProxy", on_delete=models.PROTECT)
    company = models.ForeignKey("Company", on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True)
    num_card = models.IntegerField(blank=True)
    valid_card = models.DateField(blank=True)
    cvv_card = models.IntegerField(blank=True)
    
    def __str__(self):
        return str(self.name)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name, verbose_name_plural = "Payment Method", "Payment Methods"
        ordering = ("company", "name",)
    