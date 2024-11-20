from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
import home, resume_analyzer
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('resume_analyzer/', include('resume_analyzer.urls')),
]
