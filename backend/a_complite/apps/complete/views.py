from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
import json
from rest_framework import status
from .models import Publisher, Book, Author
from rest_framework.views import APIView
from itertools import chain
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer, BookSerializerData

# Create your views here.


class BookByFieldListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        field = request.query_params['field']
        complete_field = request.query_params['input']
        if field == 'author':
            query_start = Book.objects.filter(author__name__istartswith=complete_field)
            query_regexp = Book.objects.filter(author__name__regex=r'^(.)+' + complete_field)
        elif field == 'publisher':
            query_start = Book.objects.filter(publisher__name__istartswith=complete_field)
            query_regexp = Book.objects.filter(publisher__name__regex=r'^(.)+' + complete_field)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        result_query = list(chain(query_start, query_regexp))
        serializer = BookSerializerData(result_query, many=True)
        return Response(serializer.data)


class BookByFieldsIdListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        publisher_id, author_id = None, None
        if 'author_id' in request.query_params:
            author_id = request.query_params['author_id']

        if 'publisher_id' in request.query_params:
            publisher_id = request.query_params['publisher_id']

        if not author_id:
            result_query = Book.objects.filter(author__pk=publisher_id)

        elif not publisher_id:
            result_query = Book.objects.filter(author__pk=author_id)

        else:
            print (publisher_id, author_id)
            result_query = Book.objects.filter(publisher__pk=publisher_id, author__pk=author_id)

        serializer = BookSerializerData(result_query, many=True)
        return Response(serializer.data)


class AuthorByFieldListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        complete_field = request.query_params['input']
        query_start = Author.objects.filter(name__istartswith=complete_field)
        query_regexp = Author.objects.filter(name__regex=r'^(.)+' + complete_field)
        result_query = list(chain(query_start, query_regexp))
        serializer = AuthorSerializer(result_query, many=True)
        return Response(serializer.data)


class PublisherByFieldListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        complete_field = request.query_params['input']
        query_start = Publisher.objects.filter(name__istartswith=complete_field)
        query_regexp = Publisher.objects.filter(name__regex=r'^(.)+' + complete_field)
        result_query = list(chain(query_start, query_regexp))
        serializer = PublisherSerializer(result_query, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny,)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny,)