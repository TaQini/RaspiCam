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
        r = request.POST.get('r',None).split('x')
        w,h = (r[0],r[1])
        q = request.POST.get('q',None)
        n = int(request.POST.get('n',None))
        delay = int(request.POST.get('delay',None))
        t = str((n-1)*delay*1000)
        tl = str(delay)
        # t = tl*(n-1)
        rot = request.POST.get('rot',None)
        cmd ='raspistill -w '+ w +' -h '+ h +' -t '+ t 
        cmd += ' -tl ' + tl + ' -q ' + q + ' -rot '+ rot +' -o '
        cmd += file_dir+name
        system(cmd)
        sleep(n*delay)
        ctx['name'] = name%0
        ctx['file_list'] = listdir(file_dir)
        ctx['aaa'] = (w,h,n,delay,t,tl)
    return render(request, "index.html", ctx)

