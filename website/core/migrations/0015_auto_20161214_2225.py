# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20161214_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenciador',
            name='e_mail',
            field=models.CharField(help_text='E-mail do Ag\xeanciador', max_length=255, null=True, verbose_name='E-mail', blank=True),
        ),
        migrations.AddField(
            model_name='agenciador',
            name='observacoes_telefone_celular',
            field=models.CharField(max_length=150, null=True, verbose_name='Obs. Telefone Celular', blank=True),
        ),
        migrations.AddField(
            model_name='agenciador',
            name='observacoes_telefone_residencial',
            field=models.CharField(max_length=150, null=True, verbose_name='Obs. Telefone Residencial', blank=True),
        ),
        migrations.AddField(
            model_name='agenciador',
            name='telefone_celular',
            field=models.CharField(help_text='Telefone no formato: (99) 99999-9999', max_length=15, null=True, verbose_name='Telefone Celular', blank=True),
        ),
        migrations.AddField(
            model_name='agenciador',
            name='telefone_residencial',
            field=models.CharField(help_text='Telefone no formato: (99) 9999-9999', max_length=14, null=True, verbose_name='Telefone Residencial', blank=True),
        ),
        migrations.AddField(
            model_name='corretor',
            name='e_mail',
            field=models.CharField(help_text='E-mail do Corretor', max_length=255, null=True, verbose_name='E-mail', blank=True),
        ),
        migrations.AddField(
            model_name='corretor',
            name='observacoes_telefone_celular',
            field=models.CharField(max_length=150, null=True, verbose_name='Obs. Telefone Celular', blank=True),
        ),
        migrations.AddField(
            model_name='corretor',
            name='observacoes_telefone_residencial',
            field=models.CharField(max_length=150, null=True, verbose_name='Obs. Telefone Residencial', blank=True),
        ),
        migrations.AddField(
            model_name='corretor',
            name='telefone_celular',
            field=models.CharField(help_text='Telefone no formato: (99) 99999-9999', max_length=15, null=True, verbose_name='Telefone Celular', blank=True),
        ),
        migrations.AddField(
            model_name='corretor',
            name='telefone_residencial',
            field=models.CharField(help_text='Telefone no formato: (99) 9999-9999', max_length=14, null=True, verbose_name='Telefone Residencial', blank=True),
        ),
        migrations.AddField(
            model_name='proprietario',
            name='e_mail',
            field=models.CharField(help_text='E-mail do propriet\xe1rio', max_length=255, null=True, verbose_name='E-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 14, 22, 25, 6, 611717), verbose_name='Data A\xe7\xe3o'),
        ),
    ]
