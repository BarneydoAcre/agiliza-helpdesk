from django.db import models
from default.models import Company, CompanyWorker, User



class PaymentMethod(models.Model):
    person = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, blank=True)
    num_card = models.IntegerField(blank=True)
    valid_card = models.DateField(blank=True)
    cvv_card = models.IntegerField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name, verbose_name_plural = "Payment Method", "Payment Methods"
        ordering = ("company", "name",)
 
class RequestType(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    request_name = models.CharField(max_length=25, blank=False)
        
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.request_name)

    class Meta:
        verbose_name, verbose_name_plural = "Request Type", "Requests Type"
        ordering = ("company", "request_name",)

class CustomerCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(CompanyWorker, on_delete=models.PROTECT)

    corporate_name = models.CharField(max_length=50, blank=False)
    corporate_cnpj = models.CharField(max_length=20, blank=False)
    corporate_ie = models.CharField(max_length=20, blank=False)
    corporate_email = models.CharField(max_length=50, blank=False)
    corporate_number = models.CharField(max_length=20, blank=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.corporate_name)

    class Meta:
        verbose_name, verbose_name_plural = "Customer Company", "Customers Companys"
        ordering = ("corporate_name",)

class CustomerCompanyWorker(models.Model):
    corporate = models.ForeignKey(CustomerCompany, on_delete=models.PROTECT)
    customer_name = models.CharField(max_length=50, blank=False)
    customer_cpf = models.CharField(max_length=20, blank=False)
    customer_email = models.CharField(max_length=50, blank=False)
    customer_phone = models.CharField(max_length=20, blank=False)
    customer_admin = models.BooleanField(default=False, blank=False)
    customer_staff = models.BooleanField(default=False, blank=False)
    customer_normal = models.BooleanField(default=False, blank=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.customer_name)

    class Meta:
        verbose_name, verbose_name_plural = "Customer Company Worker", "Customers Companys Workers"
        ordering = ("customer_name",)

class TicketStatus(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    status = models.CharField(max_length=127, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name, verbose_name_plural = "Ticket Status", "Ticket Status"
        ordering = ("status", "company",)

class Ticket(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(CompanyWorker, on_delete=models.PROTECT)
    title = models.CharField(max_length=255, blank=False)
    corporate = models.ForeignKey(CustomerCompany, on_delete=models.PROTECT)
    customer = models.ForeignKey(CustomerCompanyWorker, on_delete=models.PROTECT)
    type = models.ForeignKey(RequestType, on_delete=models.PROTECT)
    routine = models.CharField(max_length=255, blank=False)
    duty = models.BooleanField(default=False, blank=False)
    description_problem = models.TextField()
    status = models.ForeignKey(TicketStatus, on_delete=models.PROTECT, blank=True)
        
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name, verbose_name_plural = "Ticket", "Tickets"
        ordering = ("company", "company_worker", "title",)

class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    worker_comment = models.ForeignKey(CompanyWorker, on_delete=models.PROTECT)
    comment = models.TextField(blank=False)
        
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.ticket)

    class Meta:
        verbose_name, verbose_name_plural = "Ticket Comment", "Ticket Comments"
        ordering = ("ticket", "created",)
