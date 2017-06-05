
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Publisher, Book, Author
from rest_framework.views import APIView
from itertools import chain
from .serializers import BookSerializer

# Create your views here.


class BookByAuthorListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, complete_author, format=None):
        query_start = Book.objects.filter(author__name__istartswith=complete_author)
        query_regexp = Book.objects.filter(author__name__regex=r'^(.)+' + complete_author)
        result_query = list(chain(query_start, query_regexp))
        serializer = BookSerializer(result_query, many=True)
        return JsonResponse(serializer.data, safe=False)


class BookByPublisherListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, complete_author, format=None):
        query_start = Book.objects.filter(publisher__name__istartswith=complete_publisher)
        query_regexp = Book.objects.filter(publisher__name__regex=r'^(.)+' + complete_publisher)
        result_query = list(chain(query_start, query_regexp))
        serializer = BookSerializer(result_query, many=True)
        return JsonResponse(serializer.data, safe=False)
