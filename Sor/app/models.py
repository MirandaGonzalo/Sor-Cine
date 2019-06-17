# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Director(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateTimeField(null=False)
    
    def __str__(self):
        return '{} {}'.format(self.apellido, self.nombre)

class Pelicula(models.Model):
    DR = 'Drama'
    RO = 'Romance'
    AC = 'Accion'
    CF = 'Ciencia Ficcion'
    TR = 'Terror'
    AV = 'Aventura'
    PO = 'Policial'
    PL = 'Politica'
    FA = 'Fantasia'
    AT = 'ATP'
    M3 = '+13'
    M6 = '+16'
    M8 = '+18'
    
    GENERO_CHOICES = (
        (DR , 'Drama'),
        (RO , 'Romance'),
        (AC , 'Accion'),
        (CF , 'Ciencia Ficcion'),
        (TR , 'Terror'),
        (AV , 'Aventura'),
        (PO , 'Policial'),
        (PL , 'Politica'),
        (FA , 'Fantasia'),
    )
    
    EDADES_CHOICES = (
        (AT , 'ATP'),
        (M3 , '+13'),
        (M6 , '+16'),
        (M8 , '+18')
    )
    
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(max_length=400, null=False)
    genero = models.CharField('Genero', max_length=10, choices=GENERO_CHOICES)
    director = models.ForeignKey(Director, null=False)
    fecha_estreno = models.DateTimeField(null=False)
    portada = models.FileField(upload_to='', unique=True)
    clasificacion = models.CharField('Edades', max_length=3, choices=EDADES_CHOICES)
    duracion = models.IntegerField(null=False)
    
    def __str__(self):
        return '{} dirigida por: {}'.format(self.nombre, self.director.nombre)
    
    
class Sala(models.Model):
    numero = models.IntegerField(null=False)
    cant_asientos = models.IntegerField(null=False)
    
    def __str__(self):
        return 'Numero de Sala {}'.format(self.numero)
    
    
class asignar_Sala(models.Model):
    fecha_inicio = models.DateTimeField(null=False)
    fecha_fin = models.DateTimeField(null=False)
    pelicula = models.ForeignKey(Pelicula)
    sala = models.ForeignKey(Sala)
    en_cartelera = models.BooleanField(default=True)
    entradas_vendidas = models.IntegerField(default=0)
    
    def __str__(self):
        return 'En la Sala {} se encuentra la pelicula {}'.format(self.sala.numero, self.pelicula.nombre)
    
class Entrada(models.Model):
    cantidad = models.IntegerField(null=False, default=1)
    precio = models.IntegerField(null=False)
    sala_p = models.ForeignKey(asignar_Sala)
    
    def __str__(self):
        return '{} entradas vendidas para {} en la sala {}.'.format(self.cantidad,self.sala_p.pelicula.nombre, self.sala_p.sala.numero)
