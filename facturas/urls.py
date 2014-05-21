from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'concepto/add$',ConceptoCreateView.as_view(), name="concepto_nuevo"),
    url(r'editar/(?P<pk>\d+)/$',FacturaUpdateView.as_view(), name="factura_editar"),
    url(r'ver/(?P<pk>\d+)/$',DetailView.as_view(model=Factura), name="factura_detalle"),
    url(r'imprimir/(?P<pk>\d+)/$',FacturaImprimir.as_view(), name="factura_imprimir"),
    url(r'nueva/$',FacturaCreateView.as_view(), name="factura_nueva"),
    url(r'^$', FacturaListView.as_view(),name="factura_lista"),
)


