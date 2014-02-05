from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from models import Cliente
from views import *

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Cliente),name="cliente_lista"),
    url(r'nuevo$',CreateView.as_view(model=Cliente), name="cliente_nuevo"),
    url(r'(?P<pk>\d+)/$',DetailView.as_view(model=Cliente), name="cliente_detalle"),
)


