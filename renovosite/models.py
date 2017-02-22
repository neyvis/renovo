from __future__ import unicode_literals
from django.db import models


class About(models.Model):
    #image = models.ImageField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    #image = models.ImageField()
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    #image = models.ImageField()
    title = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title