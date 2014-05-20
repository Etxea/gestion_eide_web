from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, permission_required

from models import *
from views import *

urlpatterns = patterns('',
    url(r'^$', CursosListView.as_view(),name="cursos_lista"),
    url(r'nuevo/$',login_required(CreateView.as_view(model=Curso)), name="curso_nuevo"),
    url(r'clases/(?P<cliente_id>\d+)/nueva/$',login_required(CreateView.as_view(model=Clase)), name="clase_curso_nueva"),
    url(r'clases/nueva$',login_required(CreateView.as_view(model=Clase)), name="clase_nueva"),
    url(r'clases/(?P<pk>\d+)/editar/$',login_required(UpdateView.as_view(model=Clase)), name="clase_editar"),
    url(r'clases/(?P<pk>\d+)/borrar/$',ClaseDeleteView.as_view(), name="clase_borrar"),
    url(r'(?P<pk>\d+)/$',CursoDetailView.as_view(), name="curso_detalle"),
    url(r'(?P<pk>\d+)/borrar/$',CursoDeleteView.as_view(), name="curso_borrar"),
    url(r'(?P<pk>\d+)/editar/$',login_required(UpdateView.as_view(model=Curso)), name="curso_editar"),
)
