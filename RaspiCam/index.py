# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf
from time import time, localtime, strftime

def index(request):
    global ctx
    ctx = {}
    if request.POST:
        ctx['hello'] = request.POST['q']
    return render(request, "index.html", ctx)
