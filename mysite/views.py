from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime
#import time


def hello(request):
    return HttpResponse("Hello World")

def my_homepage_view(request):
    return HttpResponse("Home Page!!!!")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'time_ahead.html', {'offset': offset, 'dt': dt })
    
