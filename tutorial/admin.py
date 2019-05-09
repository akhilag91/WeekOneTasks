# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import nested_admin
from models import *
# Register your models here.

class BookInline(nested_admin.NestedStackedInline):
    model = Book

class PublisherAdmin(nested_admin.NestedModelAdmin):

    inlines = [BookInline]

admin.site.register(Publisher,PublisherAdmin)
