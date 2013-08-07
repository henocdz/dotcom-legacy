# -*- coding: utf-8 -*-
from django.http import Http404
from django.template import RequestContext, defaultfilters
from django.shortcuts import render_to_response, render, redirect

def home(request):
	return render_to_response('index.html',{},RequestContext(request))

def get_ajax_data(request,seccion):
	if not request.is_ajax():
		raise Http404
