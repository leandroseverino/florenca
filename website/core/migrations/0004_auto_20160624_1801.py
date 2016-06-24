# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160623_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovelrecurso',
            name='imovel',
            field=models.ForeignKey(related_name='recursos', verbose_name='Imovel', to='core.Imovel'),
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 24, 18, 1, 3, 462448), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
