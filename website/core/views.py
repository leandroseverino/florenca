from django.shortcuts import render

from .models import Imovel, ImovelRecurso, Parametro, Banner
from .serializers import (ImovelSerializer,
                          ParametroSerializer,
                          BannerSerializer,
                          ObjSerializer)

from rest_framework import mixins
from rest_framework import generics


def index(request):
    return render(request, 'index.html')


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

    queryset = ImovelRecurso.objects.\
        filter(tipo='destaque',
               imovel__finalidade_venda=u'S')
    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImovelLocacaoList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):

    queryset = ImovelRecurso.objects.\
        filter(tipo='destaque',
               imovel__finalidade_locacao=u'S')
    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
