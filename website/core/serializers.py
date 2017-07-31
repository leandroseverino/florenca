"""
Classes serializadoras utilizadas na API.
"""
from rest_framework import serializers
from .models import ImovelRecurso, Imovel, Parametro, Banner


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ('id', 'codigo', 'slug', 'descricao')


class ObjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ('id',
                  'codigo',
                  'slug',
                  'descricao',
                  'disponivel',
                  'finalidade_venda',
                  'valor',
                  'valor_venda', )


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


class ImovelRecursoSerializer(serializers.ModelSerializer):
    """
    Serializa o objeto ImovelRecurso utilizado no detalhamento do imovel.
    """
    resource_path = serializers.ReadOnlyField(source='resource')
    uploaded = serializers.ReadOnlyField(source='is_uploaded')

    class Meta:
        model = ImovelRecurso
        fields = ('id',
                  'resource_path',
                  'imovel',
                  'tipo_recurso',
                  'uploaded',
                  'descricao')


class DetalheSerializer(serializers.ModelSerializer):
    """
    Serializa o objeto Imovel e seus Recursos para a tela de Detalhamento.
    """
    recursos = ImovelRecursoSerializer(read_only=True, many=True)
    tipo_imovel_nome = serializers.ReadOnlyField()

    class Meta:
        model = Imovel
        fields = ('id',
                  'codigo',
                  'slug',
                  'descricao',
                  'disponivel',
                  'destaque',
                  'tipo_imovel_nome',
                  'finalidade_venda',
                  'finalidade_locacao',
                  'utilidade_residencial',
                  'utilidade_comercial',
                  'bairro',
                  'cidade',
                  'uf',
                  'ponto_referencia',
                  'valor',
                  'valor_venda',
                  'valor_condominio',
                  'encargos',
                  'iptu',
                  'recursos', )
