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
    exclude = ('slug',)


class ParametroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')
    exclude = ('slug',)


class AgenciadorAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class CorretorAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class ProprietarioAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class OrigemImovelAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class TipoImovelAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class RecursoInline(admin.StackedInline):
    model = ImovelRecurso
    extra = 1
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)


class ImovelAdminForm(forms.ModelForm):
    descricao = forms.CharField(widget=CKEditorWidget())
    valor = forms.DecimalField(max_digits=15,
                               decimal_places=2,
                               required=False,
                               localize=True)
    valor_condominio = forms.DecimalField(max_digits=15,
                                          decimal_places=2,
                                          required=False,
                                          localize=True)
    valor_venda = forms.DecimalField(max_digits=15,
                                     decimal_places=2,
                                     required=False,
                                     localize=True)

    class Meta:
        model = Imovel
        fields = ['valor', 'valor_condominio', 'valor_venda',]

    def clean(self):
        my_values = dict(self.data)
        has_destaque = False
        for k, v in my_values.iteritems():
            if k.startswith(u'recursos'):
                if v[0].startswith(u'destaque'):
                    if has_destaque:
                        raise forms.ValidationError('Nao pode existir mais de um recurso (foto/video) do tipo Destaque !.')
                    else:
                        has_destaque = True

        return self.cleaned_data


class ImovelAdmin(admin.ModelAdmin):
    exclude = ('slug',)
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
    # raw_id_fields = ('proprietario', 'corretor', 'agenciador')
    fieldsets = (
        ('Dados Gerais', {
            'fields': ['codigo',
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
