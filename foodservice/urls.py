from django.urls import path, include

from . import views

app_name = 'foodservice'

urlpatterns = [
    path('addProduct/', views.addProduct),
    path('getProduct/', views.getProduct),
    path('addProductItems/', views.addProductItems),
    path('addBrand/', views.addBrand),
    path('getBrand/', views.getBrand),
    path('addMeasure/', views.addMeasure),
    path('getMeasure/', views.getMeasure),
    path('addSale/', views.addSale),
    path('addSaleItems/', views.addSaleItems),
    path('addProductStock/', views.addProductStock),
    path('test/', views.getProductCost),

]