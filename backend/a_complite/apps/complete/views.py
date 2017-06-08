from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
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


class BookController(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            print('valid me')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorController(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        print (request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherController(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = PublisherSerializer(data=request.data)
        print (request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)