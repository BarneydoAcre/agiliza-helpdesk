from django.urls import path, include

from . import views

app_name = 'default'

urlpatterns = [
    path('auth/login/', views.login),
    path('addBugReport/', views.addBugReport),
]