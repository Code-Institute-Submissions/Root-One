# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

DIFFICULTY_CHOICES = (
    (str('Simple'), 'SIMPLE'),
    (str('Not too hard'), 'NOT TOO HARD'),
    (str('Tricky'), 'TRICKY'),
)


SERVES_CHOICES = [(i,i) for i in range(11)]

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    subtitle = models.TextField(max_length=400)
    serves = models.IntegerField(choices=SERVES_CHOICES, default=1)
    cooking_time = models.DurationField(blank=True, null=True)
    difficulty = models.CharField(max_length=15, choices=DIFFICULTY_CHOICES, default='Simple')
    diet_info = models.CharField(max_length=20, blank=True, null=True)
    ingredients = models.TextField()
    method = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title