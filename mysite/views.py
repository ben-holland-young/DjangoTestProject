from django.http import HttpResponse, Http404
import datetime
#import time


def hello(request):
    return HttpResponse("Hello World")

def my_homepage_view(request):
    return HttpResponse("Home Page!!!!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "It is now %s" % now
    #time.sleep(10)
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "In %s hours(s), it will be %s." % (offset, dt)
    return HttpResponse(html)
    
