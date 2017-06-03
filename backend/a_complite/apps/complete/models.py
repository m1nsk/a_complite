# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BookManager(models.Manager):
    def get_by_natural_key(self, name, author, publisher):
        return self.get(anme=name, author=author, publisher=publisher)


class Publisher(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    objects = BookManager()
    name = models.CharField(max_length=30)
    author = models.ForeignKey('Author')
    publisher = models.ForeignKey('Publisher')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'author', 'publisher')
