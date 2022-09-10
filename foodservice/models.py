from django.db import models
from django.contrib.auth.models import User

import default.models

class ProductMeasure(models.Model):
    company = models.ForeignKey(default.models.Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(default.models.CompanyWorker, on_delete=models.PROTECT)
    measure = models.CharField(max_length=2, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.measure

    class Meta:
        verbose_name, verbose_name_plural = "Unidade de Medida", "Unidades de Medida"
       
class ProductBrand(models.Model):
    company = models.ForeignKey(default.models.Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(default.models.CompanyWorker, on_delete=models.PROTECT)
    brand = models.CharField(max_length=20, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand 

    class Meta:
        verbose_name, verbose_name_plural = "Marca do Produto", "Marca dos Produtos"
        ordering = ("brand",)

class Product(models.Model):
    company = models.ForeignKey(default.models.Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(default.models.CompanyWorker, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=False)
    brand = models.ForeignKey(ProductBrand, on_delete=models.PROTECT)
    measure = models.ForeignKey(ProductMeasure, on_delete=models.PROTECT)
    stock = models.FloatField(blank=False)
    cost = models.FloatField(blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name, verbose_name_plural = "Produto", "Produtos"
        ordering = ("name",)

class ProductSale(models.Model):
    company = models.ForeignKey(default.models.Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(default.models.CompanyWorker, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name, verbose_name_plural = "Produto para Venda", "Produtos para Venda"
        ordering = ("name",)

class ProductSaleItems(models.Model):
    company = models.ForeignKey(default.models.Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(default.models.CompanyWorker, on_delete=models.PROTECT)
    product_sale = models.ForeignKey(ProductSale, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name, verbose_name_plural = "Produto Montado", "Produtos para Montados"
        ordering = ("product_sale",)
