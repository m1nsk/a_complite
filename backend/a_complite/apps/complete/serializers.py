from rest_framework import serializers
from .models import Book, Author, Publisher
import os


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name', 'id')


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ('name', 'id')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', 'image', 'author', 'publisher')


class BookSerializerData(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    author_id = serializers.PrimaryKeyRelatedField(read_only=True)
    publisher_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Book
        fields = ('name', 'image', 'author', 'author_id', 'publisher', 'publisher_id')






