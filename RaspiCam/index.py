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
        r = request.POST.get('r',None).split('x')
        w,h = (r[0],r[1])
        q = request.POST.get('q',None)
        n = int(request.POST.get('n',None))
        delay = int(request.POST.get('delay',None))
        rot = request.POST.get('rot',None)
        cmd ='raspistill -w '+ w +' -h '+ h 
        if(n!=1):
            t = str((n-1)*delay)
            tl = str(delay)
            name = 'RaspiCam-'+stamp+'-%d.jpg'
            cmd += ' -t '+ t + ' -tl ' + tl + ' -q ' + q + ' -rot '+ rot +' -o '
            ctx['name'] = name%0
        else:
            t = str(delay)
            name = 'RaspiCam-'+stamp+'-0.jpg'
            ctx['name'] = name
            cmd += ' -t ' +t + ' -q ' + q + ' -rot '+ rot +' -o '
        cmd += file_dir+name
        system(cmd)
        #if(n==1):
            #sleep(delay/800.0)
        file_list = listdir(file_dir)
        file_list.sort()
        ctx['file_list'] = file_list
        ctx['aaa'] = (cmd)
    return render(request, "index.html", ctx)

