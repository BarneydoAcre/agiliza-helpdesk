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

class AddBrandForm(forms.ModelForm):
    class Meta:
        model = models.ProductBrand
        fields = [
            "company",
            "company_worker",
            "brand",
        ]

class AddMeasureForm(forms.ModelForm):
    class Meta:
        model = models.ProductMeasure
        fields = [
            "company",
            "company_worker",
            "measure",
        ]