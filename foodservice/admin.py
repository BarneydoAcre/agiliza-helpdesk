from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ("company", "name",)
admin.site.register(models.Product, ProductAdmin)

class ProductMeasureAdmin(admin.ModelAdmin):
    list_display = ("company", "measure",)
admin.site.register(models.ProductMeasure, ProductMeasureAdmin)

class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ("company", "brand",)
admin.site.register(models.ProductBrand, ProductBrandAdmin)

class ProductSaleAdmin(admin.ModelAdmin):
    list_display = ("company", "name",)
admin.site.register(models.ProductSale, ProductSaleAdmin)
