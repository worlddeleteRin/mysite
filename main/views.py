from django.shortcuts import render
from .models import * 
from django.http import JsonResponse, HttpResponse
import urllib
import os
from django.core.files.storage import default_storage
from mysite.settings import * 
import json
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    template = 'main/index.html'
    context = {
        
    }
    return  render(request, template, context)