# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 22, 20, 14, 769620), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
