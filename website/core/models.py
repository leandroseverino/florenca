# -*- coding: utf-8 -*-
"""
Models utilizadas na app core.
"""
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.db.models.signals import pre_save
import datetime


class Banner(models.Model):
    """
    Banners
    """
    titulo = models.CharField(u'Titulo',
                              max_length=200,
                              null=False,
                              blank=False)
    slug = models.SlugField(u'Slug',
                            max_length=200,
                            unique=True)
    descricao = models.CharField(u'Descrição',
                                 max_length=255,
                                 null=False,
                                 blank=False)
    url_resource = models.CharField(u'Link/URL',
                                    max_length=200,
                                    null=True,
                                    blank=True)
    upload_resource = models.FileField('Arquivo',
                                       upload_to=u'banners',
                                       null=True,
                                       blank=True)
    action_resource = models.CharField(u'Ação ao Clicar',
                                       max_length=200,
                                       null=True,
                                       blank=True)
    ativo = models.BooleanField(u'Banner ativo',
                                default=False)

    def __unicode__(self):
        if self.url_resource:
            return " {} ".format(self.url_resource)
        elif self.upload_resource:
            return " {} ".format(self.upload_resource)

    @property
    def resource(self):
        return self.__unicode__()

    @models.permalink
    def get_absolute_url(self):
        return 'banner', [str(self.slug)]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Banner, self).save(*args, **kwargs)


class Parametro(models.Model):
    """
    Parametros genéricos do sistema.
    """
    nome = models.CharField(u'Nome',
                            null=False,
                            blank=False,
                            unique=True,
                            max_length=250)
    slug = models.SlugField(u'Slug',
                            max_length=250,
                            unique=True)
    valor = models.CharField(u'Valor',
                             null=False,
                             blank=False,
                             unique=True,
                             max_length=250)

    def __unicode__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return 'parametro', [str(self.slug)]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Parametro, self).save(*args, **kwargs)


class Agenciador(models.Model):
    """
    Agenciador de imóveis.
    """
    nome = models.CharField(u'Nome',
                            null=False,
                            blank=False,
                            unique=True,
                            max_length=250)
    slug = models.SlugField(u'Slug',
                            max_length=250,
                            unique=True)

    def __unicode__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return 'agenciador', [str(self.slug)]

    def save(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        self.slug = slugify(self.nome)
        super(Agenciador, self).save(*args, **kwargs)


class Corretor(models.Model):
    """
    Corretor de imóveis.
    """
    nome = models.CharField(u'Nome',
                            null=False,
                            blank=False,
                            unique=True,
                            max_length=250)
    slug = models.SlugField(u'Slug',
                            max_length=250,
                            unique=True)

    def __unicode__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return 'corretor', [str(self.slug)]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Corretor, self).save(*args, **kwargs)


class Proprietario(models.Model):
    """
    Proprietário de imóveis.
    """
    nome = models.CharField(u'Nome',
                            null=False,
                            blank=False,
                            unique=True,
                            max_length=250)
    slug = models.SlugField(u'Slug',
                            max_length=250,
                            unique=True)

    def __unicode__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return 'proprietario', [str(self.slug)]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Proprietario, self).save(*args, **kwargs)


class OrigemImovel(models.Model):
    """
    Origem de imóveis.
    """
    nome = models.CharField(u'Nome',
                            null=False,
                            blank=False,
                            unique=True,
                            max_length=250)
    slug = models.SlugField(u'Slug',
                            max_length=250,
                            unique=True)

    def __unicode__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return 'origem_imovel', [str(self.slug)]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(OrigemImovel, self).save(*args, **kwargs)


class TipoImovel(models.Model):
    """
    Tipo de imóveis.
    """
    nome = models.CharField(u'Nome',
                            null=False,
                            blank=False,
                            unique=True,
                            max_length=250)
    slug = models.SlugField(u'Slug',
                            max_length=250,
                            unique=True)

    nome_plural = models.CharField(u'Nome no Plural',
                            null=False,
                            blank=False,
                            unique=True,
                            max_length=250)

    def __unicode__(self):
        return self.nome

    @models.permalink
    def get_absolute_url(self):
        return 'tipo_imovel', [str(self.slug)]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(TipoImovel, self).save(*args, **kwargs)


class Imovel(models.Model):
    """
    Imóveis
    """

    SIM_NAO = ((u'S', u'Sim'),
               (u'N', u'Não'),)
    SIM_NAO_RESERVADO = ((u'S', u'Sim'),
                         (u'N', u'Não'),
                         (u'R', u'Reservado'),)
    codigo = models.CharField(u'Código',
                              max_length=10,
                              blank=False,
                              null=False)
    slug = models.SlugField(u'Slug',
                            max_length=250,
                            unique=True)
    proprietario = models.ForeignKey(Proprietario,
                                     verbose_name=u'Proprietario')
    agenciador = models.ForeignKey(Agenciador,
                                   verbose_name=u'Agenciador')
    corretor = models.ForeignKey(Corretor,
                                 verbose_name=u'Corretor')
    origem_imovel = models.ForeignKey(OrigemImovel,
                                      verbose_name=u'Origem Imovel')
    tipo_imovel = models.ForeignKey(TipoImovel,
                                    verbose_name=u'Tipo Imovel')
    finalidade_venda = models.CharField(u'Para Vender',
                                        choices=SIM_NAO,
                                        max_length=1)
    finalidade_locacao = models.CharField(u'Para Alugar',
                                          choices=SIM_NAO,
                                          max_length=1)
    utilidade_comercial = models.CharField(u'Comercial',
                                           choices=SIM_NAO,
                                           max_length=1)
    utilidade_residencial = models.CharField(u'Residêncial',
                                             choices=SIM_NAO,
                                             max_length=1)
    destaque = models.CharField(u'É destaque',
                                choices=SIM_NAO,
                                max_length=1)
    descricao = models.TextField(u'Descrição Completa do Imóvel')
    encargos = models.TextField(u'Encargos do Imóvel')
    endereco = models.CharField(u'Endereço',
                                max_length=250)
    bairro = models.CharField(u'Bairro',
                              max_length=150)
    cidade = models.CharField(u'Cidade',
                              max_length=150)
    uf = models.CharField(u'UF',
                          max_length=2)
    cep = models.CharField(u'CEP',
                           max_length=10)
    ponto_referencia = models.CharField(u'Ponto de Referência',
                                        max_length=250,
                                        blank=True,
                                        null=True)
    valor = models.DecimalField(u'Valor Locação',
                                max_digits=15,
                                decimal_places=2,
                                blank=True,
                                null=True)
    valor_condominio = models.DecimalField(u'Valor Condomínio',
                                           max_digits=15,
                                           decimal_places=2,
                                           blank=True,
                                           null=True)
    mapa = models.CharField(u'Mapa',
                            max_length=250,
                            blank=True,
                            null=True)
    valor_venda = models.DecimalField(u'Valor Venda',
                                      max_digits=15,
                                      decimal_places=2,
                                      blank=True,
                                      null=True)
    disponivel = models.CharField(u'Imóvel Disponível',
                                  choices=SIM_NAO_RESERVADO,
                                  max_length=1,
                                  blank=True,
                                  null=True)
    iptu = models.CharField(u'Tem IPTU',
                            choices=SIM_NAO,
                            max_length=1,
                            blank=True,
                            null=True)

    def __unicode__(self):
        return self.codigo

    @staticmethod
    def autocomplete_search_fields():
        return ("codigo__icontains", "descricao__icontains")

    @property
    def tipo_imovel_nome(self):
        return self.tipo_imovel.nome

    @models.permalink
    def get_absolute_url(self):
        return 'imovel', [str(self.slug)]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.codigo)
        super(Imovel, self).save(*args, **kwargs)


class ImovelRecurso(models.Model):
    """
    Recursos dos Imóveis (Fotos e Vídeos)
    """
    TIPO_RECURSO = ((u'Foto', u'Foto'),
                    (u'Video', u'Vídeo'),)

    TIPO = ((u'interno', u'Interno'),
            (u'externo', u'Externo'),
            (u'destaque', u'Destaque'),)

    imovel = models.ForeignKey(Imovel,
                               related_name='recursos',
                               verbose_name=u'Imovel')
    tipo_recurso = models.CharField(max_length=5,
                                    choices=TIPO_RECURSO,
                                    blank=True,
                                    null=True)
    tipo = models.CharField(max_length=8,
                            choices=TIPO,
                            blank=True,
                            null=True)
    url_recurso = models.CharField(u'URL/Endereço Recursos',
                                   max_length=250,
                                   blank=True,
                                   null=True)
    upload_resource = models.FileField('arquivo',
                                       upload_to=u'imovel_recurso',
                                       null=True,
                                       blank=True)
    action_resource = models.CharField(u'Ação ao Clicar',
                                       max_length=200,
                                       null=True,
                                       blank=True)
    descricao = models.CharField(u'Descrição do Recursos',
                                 max_length=250,
                                 blank=True,
                                 null=True)

    compartilha_facebook = models.BooleanField(u'Compartilha no Facebook',
                                               default=False)
    compartilha_twitter = models.BooleanField(u'Compartilha no Twitter',
                                              default=False)


    class Meta:
        verbose_name = u'Arquivo:'
        verbose_name_plural = u'Arquivos'

    def __unicode__(self):
        if self.url_recurso:
            return "{}".format(self.url_recurso)
        elif self.upload_resource:
            return "{}".format(self.upload_resource)

    @property
    def is_uploaded(self):
        return self.upload_resource.name is not u''

    @property
    def resource(self):
        return self.__unicode__()


class Log(models.Model):
    """
    Log de atividades no sistema.
    """
    usuario = models.ForeignKey(User,
                                verbose_name=u'Usuário',
                                blank=True,
                                null=True)
    operacao = models.CharField(u'Operação',
                                max_length=50)
    endereco_ip = models.CharField(u'Endereço IP',
                                   max_length=50,
                                   blank=True,
                                   null=True)
    log = models.TextField(u'Atvidade')
    data = models.DateTimeField(u'Data Ação',
                                default=datetime.datetime.now())
