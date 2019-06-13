# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

admin.site.register(Pelicula)
admin.site.register(Director)
admin.site.register(Sala)
admin.site.register(asignar_Sala)
admin.site.register(Entrada)