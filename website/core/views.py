from django.shortcuts import render

from .models import ImovelRecurso
from .serializers import ImovelSerializer

from rest_framework import mixins
from rest_framework import generics


def index(request):
    return render(request, 'index.html')


class ImovelList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):

    queryset = ImovelRecurso.objects.filter(tipo='destaque', imovel__destaque=u'S')
    serializer_class = ImovelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
