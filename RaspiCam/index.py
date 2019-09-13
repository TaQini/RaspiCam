# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from time import time, localtime, strftime
from os import system
from time import sleep

def index(request):
    ctx = {}
    if request.POST:
        now = int(time())
        stamp = strftime('%Y%m%d_%H%M%S',localtime(now))
        path = '/home/pi/RaspiCam/static/'
        name = 'RaspiCam_'+stamp+'.jpg'
        cmd = 'raspistill -w 2592 -h 1944 -t 10 -q 100 -o '
        cmd += path+name
        system(cmd)
        sleep(1)
        ctx['path'] = name
    return render(request, "index.html", ctx)
