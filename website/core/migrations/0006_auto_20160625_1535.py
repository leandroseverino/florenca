# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160625_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True, max_length=200, verbose_name='Slug')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descri\xe7\xe3o')),
                ('url_resource', models.CharField(max_length=200, null=True, verbose_name='Link/URL', blank=True)),
                ('upload_resource', models.FileField(upload_to='banners', null=True, verbose_name=b'Arquivo', blank=True)),
                ('action_resource', models.CharField(max_length=200, null=True, verbose_name='A\xe7\xe3o ao Clicar', blank=True)),
                ('ativo', models.BooleanField(default=False, verbose_name='Banner ativo')),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 25, 15, 35, 6, 210249), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
