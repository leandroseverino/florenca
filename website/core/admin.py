from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import (Agenciador,
                     Corretor,
                     Proprietario,
                     OrigemImovel,
                     TipoImovel,
                     Imovel,
                     ImovelRecurso,
                     Log)


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


class ImovelAdminForm(forms.ModelForm):
    descricao = forms.CharField(widget=CKEditorWidget())
    encargos = forms.CharField(widget=CKEditorWidget())


class ImovelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("codigo",)}
    form = ImovelAdminForm
    inlines = [RecursoInline, ]


admin.site.register(Agenciador, AgenciadorAdmin)
admin.site.register(Corretor, CorretorAdmin)
admin.site.register(Proprietario, ProprietarioAdmin)
admin.site.register(OrigemImovel, OrigemImovelAdmin)
admin.site.register(TipoImovel, TipoImovelAdmin)
admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Log)
