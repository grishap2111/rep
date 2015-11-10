# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404   
from django.http import HttpResponse
from django.template import Context, loader

import random

def index(request):
    return render_to_response('index.html')

def cameras(request):
    return render_to_response('cameras.html')