# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Publisher, Book, Author
from django.core import serializers
from itertools import chain
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
