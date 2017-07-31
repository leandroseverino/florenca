from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^api/destaques$',
        views.ImovelList.as_view()),
    url(r'^api/parametros$',
        views.ParametroList.as_view()),
    url(r'^api/banners$',
        views.BannerList.as_view()),
    url(r'^api/total_imoveis$',
        views.TotalImovelList.as_view()),
    url(r'^api/imoveis_locacao$',
        views.ImovelLocacaoList.as_view()),
    url(r'^api/imoveis_locacao/(?P<tipo>[0-9a-zA-Z_-]+)$',
        views.ImovelLocacaoList.as_view(),
        name='imovel-locacao'),
    url(r'^api/imoveis_locacao_search/$',
        views.ImovelLocacaoSearchList.as_view(),
        name='imovel-locacao-search'),
    url(r'^api/imoveis_vendas$',
        views.ImovelVendaList.as_view()),
    url(r'^api/imoveis_venda/(?P<tipo>[0-9a-zA-Z_-]+)$',
        views.ImovelVendaList.as_view(),
        name='imovel-venda'),
    url(r'^api/imoveis_venda_search/$',
        views.ImovelVendaSearchList.as_view(),
        name='imovel-venda-search'),
    url(r'^api/imovel/(?P<slug>[0-9a-zA-Z_-]+)$',
        views.ImovelDetail.as_view(),
        name='imovel-detail'),
    url(r'^api/imoveis-relacionados/(?P<slug>[0-9a-zA-Z_-]+)$',
        views.ImovelRelacionadoList.as_view(),
        name='imoveis-relacionados'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
