# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-20 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190614_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='pelicula',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.CASCADE, to='app.Pelicula'),
            preserve_default=False,
        ),
    ]