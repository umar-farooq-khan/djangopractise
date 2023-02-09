"""djangopractise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.http import HttpResponse
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('r_jobdetail/', views.r_jobdetail, name='job_detail_pg'),
    path('rfilldata/', views.rfilldata, name='applypage_html'),

    path('success/', views.success, name='success'),
    path('applied/', views.applied, name='apply_success'),

]

urlpatterns += staticfiles_urlpatterns()



