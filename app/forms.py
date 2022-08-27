from django import forms
from . import models

class AddTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = [
            'company',
            'company_worker',
            'title',
            'corporate',
            'customer',
            'type',
            'routine',
            'duty',
            'description_problem',
            'status',
        ]
        exclude = [
            'created',
            'updated',
        ]

class DeleteTicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = [
            'id',
            'company',
        ]
        exclude = [
            'created',
            'updated',
            'company_worker',
            'title',
            'corporate',
            'customer',
            'type',
            'routine',
            'duty',
            'description_problem',
            'status',
        ]

class AddTicketCommentForm(forms.ModelForm):
    class Meta:
        model = models.TicketComment
        fields = [
            'ticket',
            'worker_comment',
            'comment',
        ]
        exclude = [
            'created',
            'updated',
        ],

class DeleteTicketCommentForm(forms.ModelForm):
    class Meta:
        model = models.TicketComment
        fields = [
            'ticket',
            'worker_comment',
            'comment',
        ]
        exclude = [
            'created',
            'updated',
        ],

class AddCustomerCompanyForm(forms.ModelForm):
    class Meta:
        model = models.CustomerCompany
        fields = [
            'company',
            'company_worker',
            
            'corporate_name',
            'corporate_cnpj',
            'corporate_ie',
            'corporate_email',
            'corporate_number',
        ]
        exclude = [
            'created',
            'updated',
        ],

class AddCustomerCompanyWorkerForm(forms.ModelForm):
    class Meta:
        model = models.CustomerCompanyWorker
        fields = [
            'corporate',
            'customer_name',
            'customer_cpf',
            'customer_email',
            'customer_phone',
            'customer_admin',
            'customer_staff',
            'customer_normal',
        ]
        exclude = [
            'created',
            'updated',
        ],

class DeleteCustomerCompanyForm(forms.ModelForm):
    class Meta:
        model = models.TicketComment
        fields = [
            'ticket',
            'worker_comment',
            'comment',
        ]
        exclude = [],