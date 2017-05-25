# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Urun

# Create your views here.

def anasayfa(request):
    return render(request, 'anasayfa.html', {})

def hakkimizda(request):
    return render(request, 'hakkimizda.html', {})

def urunler(request):
    urunler = Urun.objects.order_by('isim')
    return render(request, 'urunler.html', {'urunler': urunler})

def iletisim(request):
    return render(request, 'iletisim.html', {})