# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Items(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    data = models.TextField(max_length=140)

    def __str__(self):
        return self.name