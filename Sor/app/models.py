# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Director(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fecha_nacimiento = models.DateTimeField(null=False)
    
    def __str__(self):
        return 'Director {} {} nacido en {}'.format(self.apellido, self.nombre, self.fecha_nacimiento)

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

    
    AT = 'ATP'
    M3 = '+13'
    M6 = '+16'
    M8 = '+18'
    
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
    
    def __str__(self):
        return '{} dirigida por: {}'.format(self.nombre, self.director.nombre)