from django.shortcuts import render

from django.db.models import Q
from .models import Imovel, ImovelRecurso, Parametro, Banner
from .serializers import (ImovelSerializer,
                          ParametroSerializer,
                          BannerSerializer,
                          ObjSerializer,
                          DetalheSerializer)

from rest_framework import mixins
from rest_framework import generics


def index(request):
    return render(request, 'index.html')


class ImovelDetail(generics.RetrieveAPIView):
    model = Imovel
    queryset = Imovel.objects.all()
    serializer_class = DetalheSerializer
    lookup_field = 'slug'


class ImovelRelacionadoList(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):

    def get_queryset(self):
        count_destaques = Parametro.objects.\
            filter(nome='quantidade_imoveis_relacionados')[0]
        slug = self.kwargs['slug']
        imovel = Imovel.objects.get(slug=slug)
        imoveis_relacionados = ImovelRecurso.objects.\
            filter(imovel__tipo_imovel=imovel.tipo_imovel,
                   tipo='destaque',
                   imovel__destaque=u'S').\
            exclude(imovel__id=imovel.id)[:int(count_destaques.valor)]
        return imoveis_relacionados

    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImovelList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):

    count_destaques = Parametro.objects.\
        filter(nome='quantidade_registros_destaques')[0]

    queryset = ImovelRecurso.objects.\
        filter(tipo='destaque',
               imovel__destaque=u'S').order_by('?')[:int(count_destaques.valor)]
    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ParametroList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BannerList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):

    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TotalImovelList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    queryset = Imovel.objects.all()
    serializer_class = ObjSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImovelVendaSearchList(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):

    def get_queryset(self):
        key_values = {}

        tipo = self.request.GET['tipo']

        if 'cod_imovel' in self.request.GET:
            if self.request.GET['cod_imovel'] != '':
                key_values['codigo'] = self.request.GET['cod_imovel']

        if 'modalidade' in self.request.GET:
            if self.request.GET['modalidade'] != '':
                key_values['modalidade'] = self.request.GET['modalidade']

        if 'cidade' in self.request.GET:
            if self.request.GET['cidade'] != '':
                key_values['cidade'] = self.request.GET['cidade']

        if 'bairro' in self.request.GET:
            key_values['bairro'] = self.request.GET['bairro']

        if 'dorm' in self.request.GET:
            if self.request.GET['dorm'] != '':
                key_values['dorm'] = int(self.request.GET['dorm'])

        if 'vlr_ini' in self.request.GET:
            if self.request.GET['vlr_ini'] != '':
                key_values['vlr_ini'] = float(self.request.GET['vlr_ini'])

        if 'vlr_fim' in self.request.GET:
            if self.request.GET['vlr_fim'] != '':
                key_values['vlr_fim'] = float(self.request.GET['vlr_fim'])

        q_objects = Q()

        q_objects.add(Q(tipo='destaque'), Q.AND)
        q_objects.add(Q(imovel__tipo_imovel__nome_plural=tipo), Q.AND)
        q_objects.add(Q(imovel__finalidade_venda=u'S'), Q.AND)

        for k, v in key_values.iteritems():
            if k == 'codigo':
                q_objects.add(Q(imovel__codigo=v), Q.AND)

            if k == 'modalidade':

                if v == 'Residencial':
                    q_objects.add(Q(imovel__utilidade_residencial=u'S'), Q.AND)

                elif v == 'Comercial':
                    q_objects.add(Q(imovel__utilidade_comercial=u'S'), Q.AND)

            if k == 'cidade':
                q_objects.add(Q(imovel__cidade=v), Q.AND)

            if k == 'bairro':
                q_objects.add(Q(imovel__bairro=v), Q.AND)

            # if k == 'dorm':
            #    q_objects.add(Q(qtde_dormitorios=v), Q.AND)

            if k == 'vlr_ini':
                q_objects.add(Q(imovel__valor_venda__gte=v), Q.AND)

            if k == 'vlr_fim':
                q_objects.add(Q(imovel__valor_venda__lte=v), Q.AND)

        imoveis_venda = ImovelRecurso.objects.filter(q_objects)

        return imoveis_venda

    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImovelVendaList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    def get_queryset(self):
        slug = self.kwargs['tipo']
        imoveis_venda = ImovelRecurso.objects.\
            filter(tipo='destaque',
                   imovel__finalidade_venda=u'S',
                   imovel__tipo_imovel__slug=slug)
        return imoveis_venda

    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImovelLocacaoList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):

    def get_queryset(self):
        slug = self.kwargs['tipo']

        imoveis_locacao = ImovelRecurso.objects.\
            filter(tipo='destaque',
                   imovel__finalidade_locacao=u'S',
                   imovel__tipo_imovel__slug=slug)
        return imoveis_locacao

    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImovelLocacaoSearchList(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              generics.GenericAPIView):
    """
    Classe que executa a query de filtro.
    """
    def get_queryset(self):
        key_values = {}

        tipo = self.request.GET['tipo']

        if 'cod_imovel' in self.request.GET:
            if self.request.GET['cod_imovel'] != '':
                key_values['codigo'] = self.request.GET['cod_imovel']

        if 'modalidade' in self.request.GET:
            if self.request.GET['modalidade'] != '':
                key_values['modalidade'] = self.request.GET['modalidade']

        if 'cidade' in self.request.GET:
            if self.request.GET['cidade'] != '':
                key_values['cidade'] = self.request.GET['cidade']

        if 'bairro' in self.request.GET:
            key_values['bairro'] = self.request.GET['bairro']

        if 'dorm' in self.request.GET:
            if self.request.GET['dorm'] != '':
                key_values['dorm'] = int(self.request.GET['dorm'])

        if 'vlr_ini' in self.request.GET:
            if self.request.GET['vlr_ini'] != '':
                key_values['vlr_ini'] = float(self.request.GET['vlr_ini'])

        if 'vlr_fim' in self.request.GET:
            if self.request.GET['vlr_fim'] != '':
                key_values['vlr_fim'] = float(self.request.GET['vlr_fim'])

        q_objects = Q()

        q_objects.add(Q(tipo='destaque'), Q.AND)
        q_objects.add(Q(imovel__tipo_imovel__nome_plural=tipo), Q.AND)
        q_objects.add(Q(imovel__finalidade_locacao=u'S'), Q.AND)

        for k, v in key_values.iteritems():
            if k == 'codigo':
                q_objects.add(Q(imovel__codigo=v), Q.AND)

            if k == 'modalidade':

                if v == 'Residencial':
                    q_objects.add(Q(imovel__utilidade_residencial=u'S'), Q.AND)

                elif v == 'Comercial':
                    q_objects.add(Q(imovel__utilidade_comercial=u'S'), Q.AND)

            if k == 'cidade':
                q_objects.add(Q(imovel__cidade=v), Q.AND)

            if k == 'bairro':
                q_objects.add(Q(imovel__bairro=v), Q.AND)

            # if k == 'dorm':
            #    q_objects.add(Q(qtde_dormitorios=v), Q.AND)

            if k == 'vlr_ini':
                q_objects.add(Q(imovel__valor_venda__gte=v), Q.AND)

            if k == 'vlr_fim':
                q_objects.add(Q(imovel__valor_venda__lte=v), Q.AND)

        imoveis_locacao = ImovelRecurso.objects.filter(q_objects)

        return imoveis_locacao

    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
