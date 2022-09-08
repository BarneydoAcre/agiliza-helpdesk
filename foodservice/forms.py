from django import forms

from . import models

class AddProductForm(forms.ModelForm):
    class Meta: 
        model = models.Product
        fields = [
            "company",
            "company_worker",
            "name",
            "brand",
            "measure",
            "stock",
            "cost",
        ]