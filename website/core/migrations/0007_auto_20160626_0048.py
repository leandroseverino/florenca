# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20160625_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 26, 0, 48, 50, 595818), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
