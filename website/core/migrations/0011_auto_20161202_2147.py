# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20161122_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='disponivel',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Im\xf3vel Dispon\xedvel', choices=[('S', 'Sim'), ('N', 'N\xe3o'), ('R', 'Reservado')]),
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 2, 21, 47, 31, 12628), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
