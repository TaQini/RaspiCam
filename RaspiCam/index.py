# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from time import time, localtime, strftime
from os import system,listdir
from time import sleep
from .settings import STATICFILES_DIRS

ctx = {}
file_dir = STATICFILES_DIRS[0]+'/'

def refresh():
    global ctx
    file_list = listdir(file_dir)
    file_list.remove('download')
    file_list.sort(reverse=True)
    ctx['file_list'] = file_list

def index(request):
    global ctx
    if request:
        refresh()
    if request.POST:
        # fetch args for cmd raspistill 
        now = int(time())
        stamp = strftime('%Y-%m-%d-%H%M%S',localtime(now))
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
            cmd += ' -t ' +t + ' -q ' + q + ' -rot '+ rot +' -o '
            ctx['name'] = name
        cmd += file_dir+name
        system(cmd)
        #if(n==1): # no need maybe
            #sleep(delay/800.0)
        refresh()
        # ctx['aaa'] x= (cmd)
        ctx['aaa'] = file_dir
    return render(request, "index.html", ctx)

def manage(request):
    global ctx
    if request.POST:
        pic_str = ''
        pic_list = request.POST.getlist('pic',None)
        for i in pic_list:
            pic_str += file_dir+i+' '
        if 'download' in request.POST and pic_list:
            # package pics to zip and download it
            dl = {}
            down_dir = 'download/'
            now = int(time())
            # systime = strftime('%Y-%m-%d %H:%M:%S',localtime(now))
            stamp = strftime('%Y-%m-%d-%H%M%S',localtime(now))
            file_name = 'RaspiCam-'+stamp+'.zip'
            output_file = file_dir+down_dir+file_name
            dl['name'] = file_name
            cmd  = 'zip -1 -o '+ output_file + ' '
            cmd += pic_str
            system(cmd)
            ctx['aaa'] = cmd
            return render(request, "download.html", dl)
        if 'delete' in request.POST and pic_list:
            cmd = 'rm '
            cmd += pic_str
            system(cmd)
            ctx['aaa'] = cmd
        if 'manage' in request.POST:
            pass
        refresh()
        ctx['name']=''
    return render(request, "index.html", ctx)

def clock(request):
    global ctx
    if request.POST:
        year = request.POST.get('year',None)
        month = request.POST.get('month',None)
        day = request.POST.get('day',None)
        hour = request.POST.get('hour',None)
        min = request.POST.get('min',None)
        sec = request.POST.get('sec',None)
        cmd = 'sudo date -s '
        # cmd = 'date -s '
        cmd += '"'
        cmd += '%s-%s-%s %s:%s:%s'%(year,month,day,hour,min,sec)
        cmd += '"'
        ctx['aaa'] = (cmd)
        system(cmd)
    return render(request, "index.html",ctx)
