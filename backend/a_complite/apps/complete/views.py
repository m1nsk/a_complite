# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Publisher, Book, Author
from django.core import serializers
from itertools import chain

# Create your views here.


def author_list(request, complete_author):
    if request.method == 'GET':
        query_start = Book.objects.filter(author__name__istartswith=complete_author)
        query_regexp = Book.objects.filter(author__name__regex=r'^(.)+' + complete_author)
        result_query = list(chain(query_start, query_regexp))
        data = serializers.serialize("json", result_query)
        return HttpResponse(data, content_type='application/json')


def publisher_list(request, complete_publisher):
    if request.method == 'GET':
        query_start = Book.objects.filter(publisher__name__istartswith=complete_publisher)
        query_regexp = Book.objects.filter(publisher__name__regex=r'^(.)+' + complete_publisher)
        result_query = list(chain(query_start, query_regexp))
        data = serializers.serialize("json", result_query)
        return HttpResponse(data, content_type='application/json')
