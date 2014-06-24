from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'concepto/(?P<factura_id>\d+)/add/$',ConceptoCreateView.as_view(), name="concepto_nuevo"),
    url(r'concepto/del/(?P<pk>\d+)/$',ConceptoDeleteView.as_view(), name="concepto_borrar"),
    url(r'editar/(?P<pk>\d+)/$',FacturaUpdateView.as_view(), name="factura_editar"),
    url(r'borrar/(?P<pk>\d+)/$',FacturaDeleteView.as_view(), name="factura_borrar"),
    url(r'ver/(?P<pk>\d+)/$',DetailView.as_view(model=Factura), name="factura_detalle"),
    url(r'imprimir/(?P<pk>\d+)/$',FacturaImprimir.as_view(), name="factura_imprimir"),
    url(r'nueva/$',FacturaCreateView.as_view(), name="factura_nueva"),
    url(r'^$', FacturaListView.as_view(),name="facturas_lista"),
)


