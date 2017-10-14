# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from . import views

app_name = 'dev'

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^signup/$',views.signup,name='signup'),
	url(r'^(?P<dev_id>[0-9]+)$',views.viewDev,name='viewdev'),
	url(r'^readform/$',views.readform,name = 'readform'),
	url(r'^login$',views.login,name='login'),
	url(r'^(?P<dev_id>[0-9]+)/add$',views.shareapp,name='shareapp'),
]