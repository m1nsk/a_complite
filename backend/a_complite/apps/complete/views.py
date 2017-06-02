# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Items
from django.core import serializers
from itertools import chain

# Create your views here.


def complete_list(request, complete_query):
    if request.method == 'GET':
        query_start = Items.objects.filter(name__istartswith=complete_query)
        query_regexp = Items.objects.filter(name__regex=r'^(.)+' + complete_query)
        result_query = list(chain(query_start, query_regexp))
        data = serializers.serialize("json", result_query)
        return HttpResponse(data, content_type='application/json')
