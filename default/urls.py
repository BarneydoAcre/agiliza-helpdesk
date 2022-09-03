from django.urls import path, include

from . import views

app_name = 'default'

urlpatterns = [
    path('addBugReport/', views.addBugReport),
]