# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm

# Create your models here.

WEIGHT_CHOICES = (
    ('g', 'G'),
    ('kg', 'KG'),
)

class Product(models.Model):
    name = models.CharField(max_length=300, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    weightCat = models.CharField(max_length=2, choices=WEIGHT_CHOICES, default='g')
    description = models.TextField()
    ingredients = models.TextField()
    further_info = models.TextField()

    @property
    def paypal_form(self):
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "GBP",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name

class ProductImage(models.Model):
    products = models.ForeignKey(Product, related_name='images')
    image = models.ImageField()
