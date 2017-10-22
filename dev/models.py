# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    github_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + ' - ' + self.creator.username
