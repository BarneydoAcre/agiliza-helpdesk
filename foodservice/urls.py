from django.urls import path, include

from . import views

app_name = 'foodservice'

urlpatterns = [
    path('addProduct/', views.addProduct),
    path('getProduct/', views.getProduct),
    path('addBrand/', views.addBrand),
    path('getBrand/', views.getBrand),
    path('addMeasure/', views.addMeasure),
    path('getMeasure/', views.getMeasure),
]