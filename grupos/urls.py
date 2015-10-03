from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

from django.contrib.auth.decorators import login_required, permission_required

from models import *
from views import *


urlpatterns = patterns('',
    url(r'^$', login_required(GrupoListView.as_view()),name="grupos_lista"),
    url(r'nuevo$',grupoCreateView.as_view(), name="grupo_nuevo"),
    url(r'editar/(?P<pk>\d+)/$',grupoUpdateView.as_view(), name="grupo_editar"),
    url(r'borrar/(?P<pk>\d+)/$',grupoDeleteView.as_view(), name="grupo_borrar"),
    url(r'(?P<pk>\d+)/$',grupoDetailView.as_view(), name="grupo_detalle"),

)
