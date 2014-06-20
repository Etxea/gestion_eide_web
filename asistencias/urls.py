from django.conf.urls import *
from models import *
from views import *

urlpatterns = patterns('',
    url(r'fecha/(?P<inicio_ano>\d{4})/(?P<inicio_mes>\d{2})/(?P<inicio_dia>\d{2})/(?P<fin_ano>\d{4})/(?P<fin_mes>\d{2})/(?P<fin_dia>\d{2})/$', AsistenciaListaFecha.as_view(),name="asistencias_lista_fecha"),
    url(r'curso/(?P<curso_id>\d+)/$', AsistenciaListaCurso.as_view(),name="asistencias_lista_curso"),
    url(r'cliente/(?P<cliente_id>\d+)/$', AsistenciaListaCliente.as_view(),name="asistencias_lista_cliente"),
    url(r'usuario/(?P<usuario_id>\d+)/$', AsistenciaListaUsuario.as_view(),name="asistencias_lista_profesor"),
    url(r'nueva/(?P<curso_id>\d+)/$',AsistenciaNuevaCurso.as_view(), name="asistencia_nueva_curso"),
    url(r'editar/(?P<pk>\d+)/$',AsistenciaEditar.as_view(model=Asistencia), name="asistencia_editar"),
    url(r'ver/(?P<pk>\d+)/$',AsistenciaDetalle.as_view(), name="asistencia_detalle"),
    url(r'nueva/$',AsistenciaNueva.as_view(), name="asistencia_nueva"),
    url(r'todas/$', AsistenciaLista.as_view(),name="asistencias_lista_todos"),
    url(r'mias/$', MisAsistencias.as_view(),name="asistencias_mi_lista"),


    url(r'$', AsistenciaListaPendientes.as_view(),name="asistencias_lista"),
)
