# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Urun(models.Model):
    isim = models.TextField()
    fiyat = models.FloatField()
    aciklama = models.TextField()

    def __str__(self):
        return self.isim