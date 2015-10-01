from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

from django.contrib.auth.decorators import login_required, permission_required

from models import *
from views import *


urlpatterns = patterns('',

    
    url(r'cursos^$', CursoListView.as_view(),name="cursos_lista"),
    url(r'cursos/nuevo$',CursoCreateView.as_view(), name="curso_nuevo"),
    url(r'cursos/editar/(?P<pk>\d+)/$',CursoUpdateView.as_view(), name="curso_editar"),
    url(r'cursos/borrar/(?P<pk>\d+)/$',CursoDeleteView.as_view(), name="curso_borrar"),
    url(r'cursos/(?P<pk>\d+)/$',CursoDetailView.as_view(), name="curso_detalle"),

    url(r'^$', login_required(AlumnoListView.as_view()),name="alumnos_lista"),
    url(r'nuevo$',AlumnoCreateView.as_view(), name="alumno_nuevo"),
    url(r'editar/(?P<pk>\d+)/$',AlumnoUpdateView.as_view(), name="alumno_editar"),
    url(r'borrar/(?P<pk>\d+)/$',AlumnoDeleteView.as_view(), name="alumno_borrar"),
    url(r'(?P<pk>\d+)/$',AlumnoDetailView.as_view(), name="alumno_detalle"),

)
