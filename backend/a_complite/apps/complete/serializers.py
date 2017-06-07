from rest_framework import serializers
from .models import Book, Author, Publisher
import os


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name',)


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ('name',)


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ('name', 'image', 'author', 'publisher')

    def create(self, validated_data):
        print(validated_data, 'v_data')
        author_data = validated_data['author']
        publisher_data = validated_data['publisher']
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






