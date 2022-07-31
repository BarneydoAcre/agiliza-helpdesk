from django.urls import path, include
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home),
    path(r'', include('djoser.urls.jwt')),
]