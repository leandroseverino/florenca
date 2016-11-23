# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20161111_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovelrecurso',
            name='compartilha_facebook',
            field=models.BooleanField(default=False, verbose_name='Compartilha no Facebook'),
        ),
        migrations.AddField(
            model_name='imovelrecurso',
            name='compartilha_twitter',
            field=models.BooleanField(default=False, verbose_name='Compartilha no Twitter'),
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 22, 23, 30, 42, 598383), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
