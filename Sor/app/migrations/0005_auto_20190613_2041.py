# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-13 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190613_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.asignar_Sala')),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='duracion',
            field=models.IntegerField(default=234),
            preserve_default=False,
        ),
    ]
