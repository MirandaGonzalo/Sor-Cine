# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render

def index(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'index.html', {'todas_las_peliculas':peliculas})

def datos_pelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    return render(request, 'datos_pelicula.html', {'pelicula':pelicula})