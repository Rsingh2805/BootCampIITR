# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Dev,DevPost
from django.urls import reverse

# Create your views here.

def index(request):
	return render(request,'dev/index.html')

def signup(request):
	return render(request,'dev/signup.html')

def login(request):
	try:
		dev = Dev.objects.get(dev_name=request.POST['dev_name'],dev_password=request.POST['dev_password'])
	except (KeyError,Dev.DoesNotExist):
		return render(request,'dev/index.html',{'error_message':'Username and password do not match'})
	return render(request,'dev/account.html',{'dev':dev})

def readform(request):
	dev = Dev(
			dev_name=request.POST['dev_name'],
			dev_emailid = request.POST['dev_emailid'],
			dev_password = request.POST['dev_password'],
			dev_interest = request.POST['dev_interest']
		)
	dev.save()
	return HttpResponseRedirect(reverse('dev:viewdev', args=(dev.pk,)))

def viewDev(request,dev_id):
	dev = get_object_or_404(Dev,pk=dev_id)
	return render(request,'dev/viewdev.html',{'dev':dev})

def shareapp(request,dev_id):
	dev=get_object_or_404(Dev,pk=dev_id)
	new_app = DevPost(post_name = request.POST['app_name'],creator=dev,post_link=request.POST['app_link'],post_info=request.POST['app_info'])
	try:
		new_app.save()
	except:
		return render(request,'dev/account.html',{'dev':dev,'error_message':"Couldn't add. Try again later"})
	return render(request,'dev/account.html',{'dev':dev,'error_message':"Added successfullt"})
