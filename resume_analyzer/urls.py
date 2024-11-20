

from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_analyzer, name='resume_analyzer'),
]

