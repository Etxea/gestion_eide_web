from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required

from models import Cliente
from views import *

urlpatterns = patterns('',
    url(r'^$', login_required(ListView.as_view(model=Cliente)),name="cliente_lista"),
    url(r'nuevo$',ClienteCreateView.as_view(), name="cliente_nuevo"),
    url(r'editar/(?P<pk>\d+)/$',ClienteUpdateView.as_view(), name="cliente_editar"),
    url(r'borrar/(?P<pk>\d+)/$',login_required(DeleteView.as_view(model=Cliente,success_url="/clientes/")), name="cliente_borrar"),
    url(r'contactos/(?P<cliente_id>\d+)/add/$',ClienteContactoCreateView.as_view(), name="cliente_contacto_add"),
    url(r'contactos/(?P<pk>\d+)/del/$',ClienteContactoDeleteView.as_view(), name="cliente_contacto_del"),
    url(r'ver/(?P<pk>\d+)/$',ClienteDetailView.as_view(), name="cliente_detalle"),
)
