# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Publisher, Author, Book
from django.contrib import admin

# Register your models here.


class BookInline(admin.ModelAdmin):
    model = Book


class AuthorInline(admin.StackedInline):
    inlines = [
        BookInline
    ]


class PublisherInline(admin.StackedInline):
    inlines = [
        BookInline
    ]


admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, BookInline)
