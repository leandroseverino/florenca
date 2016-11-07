from django.shortcuts import render

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
        quantidade_registros_destaque = Parametro.objects.\
            filter(nome='quantidade_imoveis_relacionados')[0]
        slug = self.kwargs['slug']
        imovel = Imovel.objects.get(slug=slug)
        imoveis_relacionados =  ImovelRecurso.objects.\
            filter(imovel__tipo_imovel=imovel.tipo_imovel,
                   tipo='destaque',
                   imovel__destaque=u'S').\
            exclude(imovel__id=imovel.id)[:int(quantidade_registros_destaque.valor)]
        return imoveis_relacionados

    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImovelList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):

    quantidade_registros_destaque = Parametro.objects.\
        filter(nome='quantidade_registros_destaques')[0]

    queryset = ImovelRecurso.objects.\
        filter(tipo='destaque',
               imovel__destaque=u'S')[:int(quantidade_registros_destaque.valor)]
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


class ImovelVendaList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):

    def get_queryset(self):
        slug = self.kwargs['tipo']

        imoveis_locacao = ImovelRecurso.objects.\
            filter(tipo='destaque',
                   imovel__finalidade_venda=u'S',
                   imovel__tipo_imovel__slug=slug)
        return imoveis_locacao


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
