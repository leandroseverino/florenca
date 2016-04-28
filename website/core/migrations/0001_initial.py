# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenciador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=250, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=250, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=250, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=250, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=10, verbose_name='C\xf3digo')),
                ('slug', models.SlugField(unique=True, max_length=250, verbose_name='Slug')),
                ('finalidade_venda', models.CharField(max_length=1, verbose_name='Para Vender', choices=[('S', 'Sim'), ('N', 'N\xe3o')])),
                ('finalidade_locacao', models.CharField(max_length=1, verbose_name='Para Alugar', choices=[('S', 'Sim'), ('N', 'N\xe3o')])),
                ('utilidade_comercial', models.CharField(max_length=1, verbose_name='Comercial', choices=[('S', 'Sim'), ('N', 'N\xe3o')])),
                ('utilidade_residencial', models.CharField(max_length=1, verbose_name='Resid\xeancial', choices=[('S', 'Sim'), ('N', 'N\xe3o')])),
                ('destaque', models.CharField(max_length=1, verbose_name='\xc9 destaque', choices=[('S', 'Sim'), ('N', 'N\xe3o')])),
                ('descricao', models.TextField(verbose_name='Descri\xe7\xe3o Completa do Im\xf3vel')),
                ('encargos', models.TextField(verbose_name='Encargos do Im\xf3vel')),
                ('endereco', models.CharField(max_length=250, verbose_name='Endere\xe7o')),
                ('bairro', models.CharField(max_length=150, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=150, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('cep', models.CharField(max_length=10, verbose_name='CEP')),
                ('ponto_referencia', models.CharField(max_length=250, null=True, verbose_name='Ponto de Refer\xeancia', blank=True)),
                ('valor', models.DecimalField(null=True, verbose_name='Valor Loca\xe7\xe3o', max_digits=15, decimal_places=2, blank=True)),
                ('valor_condominio', models.DecimalField(null=True, verbose_name='Valor Condom\xednio', max_digits=15, decimal_places=2, blank=True)),
                ('mapa', models.CharField(max_length=250, null=True, verbose_name='Mapa', blank=True)),
                ('valor_venda', models.DecimalField(null=True, verbose_name='Valor Venda', max_digits=15, decimal_places=2, blank=True)),
                ('disponivel', models.CharField(blank=True, max_length=1, null=True, verbose_name='Im\xf3vel Dispon\xedvel', choices=[('S', 'Sim'), ('N', 'N\xe3o')])),
                ('iptu', models.CharField(blank=True, max_length=1, null=True, verbose_name='Tem IPTU', choices=[('S', 'Sim'), ('N', 'N\xe3o')])),
                ('agenciador', models.ForeignKey(verbose_name='Agenciador', to='core.Agenciador')),
                ('corretor', models.ForeignKey(verbose_name='Corretor', to='core.Corretor')),
            ],
        ),
        migrations.CreateModel(
            name='ImovelRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_recurso', models.CharField(blank=True, max_length=5, null=True, choices=[('Foto', 'Foto'), ('Video', 'V\xeddeo')])),
                ('tipo', models.CharField(blank=True, max_length=8, null=True, choices=[('interno', 'Interno'), ('externo', 'Externo'), ('destaque', 'Destaque')])),
                ('url_recurso', models.CharField(max_length=250, null=True, verbose_name='URL/Endere\xe7o Recursos', blank=True)),
                ('upload_resource', models.FileField(upload_to='imovel_recurso', null=True, verbose_name=b'arquivo', blank=True)),
                ('action_resource', models.CharField(max_length=200, null=True, verbose_name='A\xe7\xe3o ao Clicar', blank=True)),
                ('descricao', models.CharField(max_length=250, null=True, verbose_name='Descri\xe7\xe3o do Recursos', blank=True)),
                ('imovel', models.ForeignKey(verbose_name='Imovel', to='core.Imovel')),
            ],
            options={
                'verbose_name': 'Arquivo:',
                'verbose_name_plural': 'Arquivos',
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operacao', models.CharField(max_length=50, verbose_name='Opera\xe7\xe3o')),
                ('endereco_ip', models.CharField(max_length=50, null=True, verbose_name='Endere\xe7o IP', blank=True)),
                ('log', models.TextField(verbose_name='Atvidade')),
                ('data', models.DateTimeField(default=datetime.datetime(2016, 4, 28, 12, 14, 22, 220723), verbose_name='Data A\xe7\xe3o')),
                ('usuario', models.ForeignKey(verbose_name='Usu\xe1rio', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrigemImovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=250, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=250, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Proprietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=250, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=250, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='TipoImovel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=250, verbose_name='Nome')),
                ('slug', models.SlugField(unique=True, max_length=250, verbose_name='Slug')),
            ],
        ),
        migrations.AddField(
            model_name='imovel',
            name='origem_imovel',
            field=models.ForeignKey(verbose_name='Origem Imovel', to='core.OrigemImovel'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='proprietario',
            field=models.ForeignKey(verbose_name='Proprietario', to='core.Proprietario'),
        ),
        migrations.AddField(
            model_name='imovel',
            name='tipo_imovel',
            field=models.ForeignKey(verbose_name='Tipo Imovel', to='core.TipoImovel'),
        ),
    ]
