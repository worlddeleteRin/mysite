
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('aboutus', views.aboutus, name = 'aboutus'),
    path('contacts', views.contacts, name = 'contacts'),
    path('web_dev', views.web_dev, name = 'web_dev'),
    path('design', views.design, name = 'design'),
    path('adv', views.adv, name = 'adv'),
    path('call_request', views.call_request, name = 'call_request'),
    path('politica', views.politica, name = 'politica'),
]
