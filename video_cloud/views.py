# -*- coding: utf-8 -*-
import random
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, loader


def index(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('index.html', args)

def cameras(request):
    args = {'username': auth.get_user(request).username}
    return render_to_response('cameras.html', args)
