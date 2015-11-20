# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 16:31:34 2015

@author: lk132_000
"""

from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")
    
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)