# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20161029_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoimovel',
            name='nome_plural',
            field=models.CharField(default=1, unique=True, max_length=250, verbose_name='Nome no Plural'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 11, 1, 31, 46, 504875), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
