# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ProductImage
from django.contrib import admin
from .models import Product

# Register your models here.

admin.site.register(Product)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]

