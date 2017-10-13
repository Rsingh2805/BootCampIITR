# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dev(models.Model):
	dev_name = models.CharField(max_length=50)
	dev_emailid = models.CharField(max_length=100)
	dev_password = models.CharField(max_length=20)
	dev_interest = models.CharField(max_length=1000)

class DevPost(models.Model):
	creator = models.ForeignKey(Dev,on_delete=models.CASCADE)
	post_info = models.CharField(max_length=1000)
	post_link = models.CharField(max_length=500)