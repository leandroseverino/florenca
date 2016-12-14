# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20161214_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 14, 22, 8, 3, 689482), verbose_name='Data A\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='observacoes_telefone_celular',
            field=models.CharField(max_length=150, null=True, verbose_name='Obs. Telefone Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='observacoes_telefone_residencial',
            field=models.CharField(max_length=150, null=True, verbose_name='Obs. Telefone Residencial', blank=True),
        ),
    ]
