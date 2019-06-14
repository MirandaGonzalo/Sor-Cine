# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

def index(request): 
    peliculas = asignar_Sala.objects.filter(en_cartelera=True).order_by('pelicula__nombre')    
    entradas = Entrada.objects.all()
    for a in entradas:
        print a.cantidad
    return render(request, 'index.html', {'todas_las_peliculas':peliculas})

def datos_pelicula(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    salas = asignar_Sala.objects.filter(pelicula=pelicula, en_cartelera=True)
    return render(request, 'datos_pelicula.html', {'pelicula':pelicula, 'salas_disponibles':salas})

def compra_entradas(request, id_pelicula):
    pelicula = Pelicula.objects.get(id=id_pelicula)
    
    opciones_salas = asignar_Sala.objects.filter(pelicula=pelicula, en_cartelera=True)
    return render(request, 'comprar_entrada.html', {'pelicula':pelicula, 'todas_las_salas':opciones_salas})

def compra(request):
    if request.method == "POST":
        cant_entradas = request.POST['cant_entradas']
        precio = request.POST['precio']
        id_sala = request.POST['id_sala']
        id_peli = request.POST['id_peli']
        sala = Sala.objects.get(id=id_sala)
        id_sala2 = sala.id
        pelicula = Pelicula.objects.get(id=id_peli) 
        limite = sala.cant_asientos
        vendidas = 0
        entradas = Entrada.objects.filter(sala__id=id_sala2)
        for a in entradas:
            total = a.cantidad
            vendidas += total
        disponible = (limite-vendidas)
        vend = int(vendidas)
        can = int(cant_entradas)
        a = vend + can
        if (a > limite):
            msg = "No hay suficientes asientos disponibles."
        else:
            print ("llega")
            entrada = Entrada(cantidad=can, sala=sala, precio=precio)
            entrada.save()
            msg = "Entradas compradas con exito."
        data = {
            'resultado': msg
        }
        return JsonResponse(data)
    
    return render(request, 'index.html')