# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20161202_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agenciador',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='banner',
            options={'ordering': ['titulo']},
        ),
        migrations.AlterModelOptions(
            name='corretor',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='origemimovel',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='parametro',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='proprietario',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='tipoimovel',
            options={'ordering': ['nome']},
        ),
        migrations.AddField(
            model_name='proprietario',
            name='observacoes',
            field=models.TextField(null=True, verbose_name='Observa\xe7\xf5es', blank=True),
        ),
        migrations.AddField(
            model_name='proprietario',
            name='observacoes_telefone_celular',
            field=models.CharField(max_length=150, null=True, verbose_name='Observa\xe7\xf5es', blank=True),
        ),
        migrations.AddField(
            model_name='proprietario',
            name='observacoes_telefone_residencial',
            field=models.CharField(max_length=150, null=True, verbose_name='Observa\xe7\xf5es', blank=True),
        ),
        migrations.AddField(
            model_name='proprietario',
            name='telefone_celular',
            field=models.CharField(max_length=15, null=True, verbose_name='Telefone Celular', blank=True),
        ),
        migrations.AddField(
            model_name='proprietario',
            name='telefone_residencial',
            field=models.CharField(max_length=14, null=True, verbose_name='Telefone Residencial', blank=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 14, 22, 0, 10, 818629), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
