from django.conf.urls import *
#from django.views.generic import ListView, CreateView, UpdateView
from models import *
from views import *

urlpatterns = patterns('',
   
    url(r'partes/nuevo/$',ParteNuevo.as_view(), name="parte_nuevo"),
    url(r'partes/nuevo/(?P<cliente_id>\d+)/$',ParteNuevoCliente.as_view(), name="parte_nuevo_cliente"),
    url(r'partes/editar/(?P<pk>\d+)/$',ParteEditar.as_view(model=Parte), name="parte_editar"),
    url(r'partes/ver/(?P<pk>\d+)/$',ParteDetalle.as_view(), name="parte_detalle"),
    url(r'partes/$', ParteLista.as_view(),name="partes_lista"),
    url(r'partes/mios/$', MisPartes.as_view(),name="partes_mi_lista"),
    url(r'partes/cliente/(?P<cliente_id>\d+)/$', ParteListaCliente.as_view(),name="partes_lista_cliente"),
    url(r'partes/usuario/(?P<usuario_id>\d+)/$', ParteListaUsuario.as_view(),name="partes_lista_usuario"),
#    url(r'bonos$', ListView.as_view(model=Bono),name="bonos_lista"),
#    url(r'bonos/nuevo$',CreateView.as_view(model=Bono), name="bono_nuevo"),
#    url(r'bonos/(?P<pk>\d+)/$',UpdateView.as_view(model=Bono), name="bono_editar"),
)
