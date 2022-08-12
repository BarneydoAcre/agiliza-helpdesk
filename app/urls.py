from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('auth/login/', views.login),
    path('getCompany/', views.getCompany),
    path('auth/', include('djoser.urls.jwt')),
]