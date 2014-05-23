from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required

from models import Cliente
from views import *

urlpatterns = patterns('',
    url(r'^$', login_required(ListView.as_view(model=Cliente)),name="cliente_lista"),
    url(r'nuevo$',login_required(CreateView.as_view(model=Cliente)), name="cliente_nuevo"),
    url(r'editar/(?P<pk>\d+)/$',login_required(UpdateView.as_view(model=Cliente)), name="cliente_editar"),
    url(r'borrar/(?P<pk>\d+)/$',login_required(DeleteView.as_view(model=Cliente,success_url="/clientes/")), name="cliente_borrar"),
    url(r'(?P<pk>\d+)/$',login_required(DetailView.as_view(model=Cliente)), name="cliente_detalle"),
)
