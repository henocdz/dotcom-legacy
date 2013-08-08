# -*- coding: utf-8 -*-
from django.http import Http404
from django.template import RequestContext, defaultfilters
from django.shortcuts import render_to_response, render, redirect
from dzuno import models as Dz
def home(request):

	usuario = Dz.Me.objects.get(pk=1)
	cursos = Dz.Course.objects.all().order_by('-date')
	proyectos = Dz.Project.objects.all().order_by('-date')
	return render_to_response('index.html',{'usr': usuario, 'courses': cursos, 'projects': proyectos},RequestContext(request))

def get_ajax_data(request,seccion):
	if not request.is_ajax():
		raise Http404
