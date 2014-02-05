from django.conf.urls.defaults import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from models import Factura, Concepto

urlpatterns = patterns('',
    url(r'concepto/add$',CreateView.as_view(model=Concepto), name="concepto_nuevo"),
    url(r'(?P<pk>\d+)/$',DetailView.as_view(model=Factura), name="factura_detalle"),
    url(r'add/$',CreateView.as_view(model=Factura), name="factura_nueva"),
    url(r'^$', ListView.as_view(model=Factura),name="factura_lista"),

)


