# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dev/',include('dev.urls'))
]
