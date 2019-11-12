"""fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

import mainapp.views as mainapp

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('personal/', include('personalapp.urls', namespace='personal')),
    path('admin/', include('adminapp.urls', namespace='admin')),
    #path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

