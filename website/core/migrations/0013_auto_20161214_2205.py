# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20161214_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 14, 22, 5, 52, 658625), verbose_name='Data A\xe7\xe3o'),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='telefone_celular',
            field=models.CharField(help_text='Telefone no formato: (99) 99999-9999', max_length=15, null=True, verbose_name='Telefone Celular', blank=True),
        ),
        migrations.AlterField(
            model_name='proprietario',
            name='telefone_residencial',
            field=models.CharField(help_text='Telefone no formato: (99) 9999-9999', max_length=14, null=True, verbose_name='Telefone Residencial', blank=True),
        ),
    ]
