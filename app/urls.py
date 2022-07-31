from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home),
    path('', include('djoser.urls.jwt')),
]