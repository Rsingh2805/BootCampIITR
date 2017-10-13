# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import Dev
from django.urls import reverse

# Create your views here.

def index(request):
	return render(request,'dev/index.html')

def signup(request):
	return render(request,'dev/signup.html')

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

