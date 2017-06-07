from rest_framework import serializers
from .models import Book, Author, Publisher
import os


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField()


class PublisherSerializer(serializers.Serializer):
    name = serializers.CharField()


class BookSerializer(serializers.Serializer):
    name = serializers.CharField()
    image = serializers.ImageField(required=False)
    author = AuthorSerializer(many=True)
    publisher = PublisherSerializer(many=True)

    def create(self, validated_data):
        print(validated_data, 'v_data')
        author_data = validated_data.pop('author')
        publisher_data = validated_data.pop('publisher')
        author = Author.objects.filter(name=author_data).first()
        if author == None:
            author = Author.objects.create(name=author_data)

        publisher = Publisher.objects.filter(name=publisher_data).first()
        if publisher == None:
            publisher = Publisher.objects.create(name=publisher_data)

        name = validated_data['name']
        image = ''
        if image in validated_data:
            image = validated_data['image']
        return Book.objects.create(name=name, image=image, author=author, publisher=publisher)

    def update(self, instance, validated_data):
        print('update')






