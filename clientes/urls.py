from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required, permission_required

from models import Cliente
from views import *

urlpatterns = patterns('',
    url(r'^$', login_required(ListView.as_view(model=Cliente)),name="cliente_lista"),
    url(r'nuevo$',login_required(CreateView.as_view(model=Cliente)), name="cliente_nuevo"),
    url(r'(?P<pk>\d+)/$',login_required(DetailView.as_view(model=Cliente)), name="cliente_detalle"),
    url(r'editar/(?P<pk>\d+)/$',login_required(UpdateView.as_view(model=Cliente)), name="cliente_editar"),
)
