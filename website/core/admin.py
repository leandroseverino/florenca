from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import (Banner,
                     Parametro,
                     Agenciador,
                     Corretor,
                     Proprietario,
                     OrigemImovel,
                     TipoImovel,
                     Imovel,
                     ImovelRecurso,
                     Log)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'ativo')
    prepopulated_fields = {"slug": ("titulo",)}


class ParametroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')
    prepopulated_fields = {"slug": ("nome",)}


class AgenciadorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


class CorretorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


class ProprietarioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


class OrigemImovelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


class TipoImovelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}


class RecursoInline(admin.StackedInline):
    model = ImovelRecurso
    extra = 1


class ImovelAdminForm(forms.ModelForm):
    descricao = forms.CharField(widget=CKEditorWidget())


class ImovelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("codigo",)}
    list_display = ('codigo',
                    'proprietario',
                    'tipo_imovel',
                    '_descricao',
                    'finalidade_venda',
                    'finalidade_locacao',
                    'utilidade_comercial',
                    'utilidade_residencial',
                    'destaque',
                    'uf',
                    'cidade',
                    'bairro',
                    'disponivel')
    search_fields = ['codigo',
                     'descricao',
                     'uf',
                     'cidade',
                     'bairro']
    list_filter = ('uf',
                   'cidade',
                   'bairro')
    raw_id_fields = ('proprietario', 'corretor', 'agenciador')
    fieldsets = (
        ('Dados Gerais', {
            'fields': ['codigo',
                       'slug',
                       'descricao',
                       'destaque',
                       'disponivel']
        }),
        ('Pessoas', {
            'classes': ('wide','extrapretty'),
            'fields': ['proprietario', 'agenciador', 'corretor']
        }),
        ('Origens', {
            'fields': ['origem_imovel']
        }),
        ('Tipo', {
            'fields': ['tipo_imovel']
        }),
        ('Aplicacao', {
            'fields': ['finalidade_venda', 'finalidade_locacao', 'utilidade_comercial', 'utilidade_residencial']
        }),
        ('Localizacao', {
            'fields': ['endereco', 'bairro', 'cidade', 'uf', 'cep', 'ponto_referencia', 'mapa']
        }),
        ('Financeiro', {
            'fields': ['encargos', 'iptu', 'valor', 'valor_condominio', 'valor_venda']
        }),
    )
    form = ImovelAdminForm
    inlines = [RecursoInline, ]

    def _descricao(self, obj):
        return obj.descricao

    _descricao.short_description = 'Descricao'

    _descricao.allow_tags = True

admin.site.register(Banner, BannerAdmin)
admin.site.register(Parametro, ParametroAdmin)
admin.site.register(Agenciador, AgenciadorAdmin)
admin.site.register(Corretor, CorretorAdmin)
admin.site.register(Proprietario, ProprietarioAdmin)
admin.site.register(OrigemImovel, OrigemImovelAdmin)
admin.site.register(TipoImovel, TipoImovelAdmin)
admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Log)
