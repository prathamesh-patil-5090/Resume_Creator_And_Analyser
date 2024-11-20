from django.contrib import admin
from django.urls import path, include
import resume_analyzer.views as res

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.gen_resume, name='gen_resume'),
    path('analysis/', views.analysis, name='resume_analyzer'),
]
