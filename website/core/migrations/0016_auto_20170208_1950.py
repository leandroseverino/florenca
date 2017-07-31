# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20161214_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 8, 19, 50, 43, 730777), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
