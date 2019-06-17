# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import xlwt

def index(request): 
    peliculas = asignar_Sala.objects.filter(en_cartelera=True).order_by('pelicula__nombre')
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
        sala_a = asignar_Sala.objects.get(pelicula=pelicula, sala=sala)
        limite = sala.cant_asientos
        vendidas = 0
        entradas = Entrada.objects.filter(sala_p=sala_a)
        for a in entradas:
            total = a.cantidad
            vendidas += total

        disponible = (limite-vendidas)
        vend = int(vendidas)
        can = int(cant_entradas)
        a = vend + can
        estado = 0
        if (a > limite):
            msg = "No hay suficientes asientos disponibles."
        else:
            entrada = Entrada(cantidad=can,precio=precio, sala_p=sala_a)
            entrada.save()
            sala_a.entradas_vendidas += entrada.cantidad
            sala_a.save()
            msg = "Entradas compradas con exito."
            estado = 1
        data = {
            'resultado': msg,
            'estado':estado
        }
        return JsonResponse(data)
    
    return render(request, 'index.html')

def ver_peliculas(request):
    pelicula = Pelicula.objects.all()
    print pelicula
    return render(request, 'peliculas.html', {'todas_las_peliculas':pelicula})

def salas(request):
    salas = Sala.objects.all().order_by('numero')
    return render(request, 'salas.html', {'salas':salas})

def salas_asignadas(request, id_sala):
    sala_elegida = Sala.objects.get(id=id_sala)
    salas_asignadas = asignar_Sala.objects.filter(sala__id=id_sala, en_cartelera=True).order_by('pelicula__nombre')
    for a in salas_asignadas:
        print a.entradas_vendidas
    return render(request, 'salas_asig.html', {'salas_asignadas':salas_asignadas, 'sala':sala_elegida})

def generar_informe(request, id_sala_a):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="datos_sala.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0
    row_num2 = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Pelicula', 'Entradas Vendidas']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()


    rows = asignar_Sala.objects.filter(sala__id=id_sala_a).values_list('pelicula__nombre', 'entradas_vendidas').order_by('entradas_vendidas')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
