# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from time import time, localtime, strftime
from os import system,listdir
from time import sleep

def index(request):
    ctx = {}
    if request.POST:
        now = int(time())
        stamp = strftime('%Y-%m-%d_%H%M%S',localtime(now))
        file_dir = 'static/'
        name = 'RaspiCam-'+stamp+'.jpg'
        cmd = 'raspistill -w 2592 -h 1944 -t 10 -q 500 -o '
        cmd += file_dir+name
        system(cmd)
        sleep(1)
        ctx['name'] = name
        ctx['file_list'] = listdir(file_dir)
    return render(request, "index.html", ctx)
