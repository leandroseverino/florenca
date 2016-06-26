# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160624_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=250, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=250, verbose_name='Slug')),
                ('valor', models.CharField(unique=True, max_length=250, verbose_name='Valor')),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 25, 13, 50, 39, 449440), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
