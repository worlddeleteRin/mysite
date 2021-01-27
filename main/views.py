from django.shortcuts import render
from .models import * 
from django.http import JsonResponse, HttpResponse
import urllib
import os
from django.core.files.storage import default_storage
from mysite.settings import * 
import json
from django.template.loader import render_to_string
from datetime import datetime
from .telegrambot import *

# Create your views here.

def index(request):
    template = 'main/index.html'
    context = {
        
    }
    return  render(request, template, context)

def aboutus(request):
    template = 'main/aboutus.html'
    context = {

    }
    return render(request, template, context)

def contacts(request):
    template = 'main/contacts.html'
    context = {

    }
    return render(request, template, context)
    

def web_dev(request):
    template = 'main/web_dev.html'
    context = {

    }
    return render(request, template, context)

def design(request):
    template = 'main/design.html'
    context = {
        
    }
    return render(request, template, context)

def adv(request):
    template = 'main/adv.html'
    context = {
        
    }
    return render(request, template, context)
    
    
def call_request(request):
    time = datetime.now()
    time = time.strftime("%Y-%m-%d-%H:%M")
    current_time = f'Время заявки: {time} \n'
    call_type = request.GET['call_type']
    if call_type == 'project':
        call_name = request.GET['call_name']
        call_phone = request.GET['call_phone']
        call_mail = request.GET['call_mail']
        call_about = request.GET['call_about']
        final_message =  '🔥 Заявка на обратный звонок 🔥 \n' + 'Сайт: mysite \n' + 'Тип: {} \n'.format(call_type) + f'Имя: {call_name} \n' + f'Телефон: {call_phone} \n' + f'Почта: {call_mail} \n' + f'О проекте: {call_about} \n' + current_time
        send_message(final_message)
    if call_type == 'phone_only':
        call_phone = request.GET['call_phone']
        final_message =  '🔥 Заявка на обратный звонок 🔥 \n' + 'Сайт: mysite \n' + 'Тип: {} \n'.format(call_type) + f'Телефон: {call_phone} \n' + current_time
        send_message(final_message)
    return JsonResponse({
        'send': True,
    }, status = 200)

def politica(request):
    template = 'main/politica.html'
    context = {

    }
    return render(request, template, context)
    
