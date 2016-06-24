# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160623_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 23, 5, 24, 769559), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
