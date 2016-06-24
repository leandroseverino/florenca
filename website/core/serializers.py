from rest_framework import serializers
from .models import ImovelRecurso, Imovel


class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ('codigo', 'slug', 'descricao')


class ImovelSerializer(serializers.ModelSerializer):

    imovel = ObjSerializer(many=False, read_only=True)
    resource_path = serializers.ReadOnlyField(source='resource')

    class Meta:
        model = ImovelRecurso
        fields = ('resource_path', 'imovel')
