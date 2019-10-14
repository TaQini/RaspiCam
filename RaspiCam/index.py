# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from os import system,listdir
from .settings import STATICFILES_DIRS

ctx = {}
file_dir = STATICFILES_DIRS[0]+'/'
down_dir = file_dir+'download/'

def refresh():
    global ctx
    file_list = listdir(file_dir)
    file_list.remove('download')
    file_list.sort(reverse=True)
    ctx['file_list'] = file_list

def index(request):
    global ctx
    ctx['no_pic_selected'] = False
    if request:
        refresh()
    if request.POST:
        # fetch args for cmd raspistill 
        sys_year = int(request.POST.get('sys_year',None))
        sys_month = int(request.POST.get('sys_month',None))
        sys_day = int(request.POST.get('sys_day',None))
        sys_hour = int(request.POST.get('sys_hour',None))
        sys_min = int(request.POST.get('sys_min',None))
        sys_sec = int(request.POST.get('sys_sec',None))
        stamp = '%4d%02d%02d_%02d%02d%02d'%(sys_year, sys_month, sys_day, sys_hour, sys_min, sys_sec)

        pic_list = request.POST.getlist('picture',None)
        l = []
        for i in pic_list:
            l.append(file_dir+i)
        pic_str = ' '.join(l)

        if 'capture' in request.POST:
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
                name = 'RaspiCam-'+stamp+'-%04d.jpg'
                cmd += ' -t '+ t + ' -tl ' + tl + ' -q ' + q + ' -rot '+ rot +' -o '
            else:
                t = str(delay)
                name = 'RaspiCam-'+stamp+'-0.jpg'
                cmd += ' -t ' +t + ' -q ' + q + ' -rot '+ rot +' -o '
            cmd += file_dir+name
            system(cmd)
            refresh()
            ctx['aaa'] = (cmd)

        if 'download' in request.POST:
            if not pic_list:
                ctx['no_pic_selected'] = True
            else:
                # package pics to zip and download it
                dl = {}
                file_name = 'RaspiCam_'+stamp+'.zip'
                output_file = down_dir+file_name
                dl['name'] = file_name
                cmd  = 'zip -1 -j -o '+ output_file + ' '
                cmd += pic_str
                system(cmd)
                ctx['aaa'] = cmd
                return render(request, "download.html", dl)
        if 'delete' in request.POST:
            if not pic_list:
                ctx['no_pic_selected'] = True
            else:
                cmd = 'rm '
                cmd += pic_str
                system(cmd)
                ctx['aaa'] = cmd
        if 'manage' in request.POST:
            ctx['aaa'] = 'debug :',pic_str,ctx['no_pic_selected']
        refresh()
    return render(request, "index.html", ctx)

def manage(request):
    m = {}
    m['no_file_selected'] = False
    if request.POST:
        checked_file_list = request.POST.getlist('dl_file',None)
        l = []
        for i in checked_file_list:
            l.append(down_dir+i)
        file_str = ' '.join(l)
        if 'delete' in request.POST:
            if not file_str:
                m['no_file_selected'] = True
            else:
                cmd = 'rm '
                cmd += file_str
                system(cmd)
                m['aaa'] = cmd,file_str
    m['dl_file_list'] = listdir(down_dir)
    return render(request, "manage",m)
