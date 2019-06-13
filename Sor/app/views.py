# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render

def index(request): 
    peliculas = asignar_Sala.objects.filter(en_cartelera=True).order_by('pelicula__nombre')    
    
    return render(request, 'index.html', {'todas_las_peliculas':peliculas})

def datos_pelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    salas = asignar_Sala.objects.filter(pelicula=pelicula, en_cartelera=True)
    return render(request, 'datos_pelicula.html', {'pelicula':pelicula, 'salas_disponibles':salas})

def compra_entradas(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    return render(request, 'comprar_entrada.html', {'pelicula':pelicula})