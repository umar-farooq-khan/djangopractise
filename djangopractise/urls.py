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
    path('job_detail/<int:id>', views.job_detail, name='job_detail_pg'),
    path('apply_form/<int:id>', views.apply_form, name='applypage_html'),
    path('applied/', views.applied, name='apply_success'),
    path('success/', views.success, name='apply_success_already_filled'),

    path('load-more/', views.load_more, name='load-more'),
    path('your_django_function/', views.your_django_function, name='your_django_function'),
    path('contact-us/', views.contact_us, name='contact_us'),

]

urlpatterns += staticfiles_urlpatterns()



