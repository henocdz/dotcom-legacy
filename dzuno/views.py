# -*- coding: utf-8 -*-
from django.http import Http404
from django.template import RequestContext, defaultfilters
from django.shortcuts import render_to_response, render, redirect
from dzuno import models as Dz
from django.core.mail import send_mail,BadHeaderError
from django.core.validators import email_re
import json
def home(request):

	usuario = Dz.Me.objects.get(pk=1)
	cursos = Dz.Course.objects.all().order_by('-date')
	proyectos = Dz.Project.objects.all().order_by('-date')
	return render_to_response('index.html',{'usr': usuario, 'courses': cursos, 'projects': proyectos},RequestContext(request))

def send_email(request):
	if not request.method == "POST":
		raise Http404

	p = request.POST
	try:
		name = p.get('_name','')
		email = p.get('_email','')
		s = p.get('_subject','')
		m = p.get('_message','')
	except:
		return render_to_response('ajaxresponse.html',{'data':json.dumps( { 'status': { 'no':2 } } ) })


	if (not name) or (not s) or (not m):
		return render_to_response('ajaxresponse.html',{'data':json.dumps( { 'status': { 'no':2 } } ) })
	elif not email_re.match(email):
		return render_to_response('ajaxresponse.html',{'data':json.dumps( { 'status': { 'no':2} } ) })


	try:
		send_mail(s,m,email,['henocdz@gmail.com'])
	except BadHeaderError:
		return render_to_response('ajaxresponse.html',{'data':json.dumps( { 'status': { 'no':2} } ) })
	

	return render_to_response('ajaxresponse.html',{'data':json.dumps( { 'status': { 'no':1} } ) })




def get_ajax_data(request,seccion):
	if not request.is_ajax():
		raise Http404
