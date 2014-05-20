from django.conf.urls import *
#from django.views.generic import ListView, CreateView, UpdateView
from models import *
from views import *

urlpatterns = patterns('',

    url(r'asistencia/nuevo/$',AsistenciaNuevo.as_view(), name="asistencia_nuevo"),
    #url(r'asistencia/nuevo/(?P<cliente_id>\d+)/$',AsistenciaNuevoCliente.as_view(), name="Asistencia_nuevo_cliente"),
    url(r'asistencia/editar/(?P<pk>\d+)/$',AsistenciaEditar.as_view(model=Asistencia), name="asistencia_editar"),
    url(r'asistencia/ver/(?P<pk>\d+)/$',AsistenciaDetalle.as_view(), name="asistencia_detalle"),
    url(r'asistencia/$', AsistenciaListaPendientes.as_view(),name="asistencias_lista"),
    url(r'asistencia/todos/$', AsistenciaLista.as_view(),name="asistencias_lista_todos"),
    url(r'asistencia/mios/$', MisAsistencias.as_view(),name="asistencias_mi_lista"),
    url(r'asistencia/cliente/(?P<curso_id>\d+)/$', AsistenciaListaCurso.as_view(),name="asistencia_lista_curso"),
    url(r'asistencia/usuario/(?P<usuario_id>\d+)/$', AsistenciaListaUsuario.as_view(),name="asistencias_lista_usuario"),

)
