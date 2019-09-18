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
        stamp = strftime('%Y-%m-%d-%H%M%S',localtime(now))
        file_dir = 'static/'
        name = 'RaspiCam-'+stamp+'-%d.jpg'
        w = '2592'
        h = '1944'
        q = '100'
        t = '200'
        l = '1000'
        rot = '180'
        cmd ='raspistill -w '+ w +' -h '+ h +' -t '+ t 
        cmd += ' -l ' + l + ' -q ' + q + ' -rot '+ rot +' -o '
        cmd += file_dir+name
        system(cmd)
        sleep(1)
        ctx['name'] = name
        ctx['file_list'] = listdir(file_dir)
    return render(request, "index.html", ctx)
