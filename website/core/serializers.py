from rest_framework import serializers
from .models import ImovelRecurso, Imovel, Parametro, Banner


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ('id', 'codigo', 'slug', 'descricao')


class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ('id', 'codigo', 'slug', 'descricao')


class ImovelSerializer(serializers.ModelSerializer):

    imovel = ObjSerializer(many=False, read_only=True)
    resource_path = serializers.ReadOnlyField(source='resource')
    uploaded = serializers.ReadOnlyField(source='is_uploaded')

    class Meta:
        model = ImovelRecurso
        fields = ('resource_path', 'imovel', 'tipo_recurso', 'uploaded')


class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametro
        fields = ('nome', 'valor')


class BannerSerializer(serializers.ModelSerializer):
    resource_path = serializers.ReadOnlyField(source='resource')

    class Meta:
        model = Banner
        fields = ('id', 'descricao', 'resource_path')
