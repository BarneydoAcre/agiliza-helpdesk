from django.urls import path, include

from . import views

app_name = 'foodservice'

urlpatterns = [
    path('addProduct/', views.addProduct),
    path('getProduct/', views.getProduct),
    path('getBrand/', views.getBrand),
    path('getMeasure/', views.getMeasure),
]