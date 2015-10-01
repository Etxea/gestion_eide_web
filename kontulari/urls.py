from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from views import *
from django.contrib import admin

# from asistencias.api import AsistenciaResource
#asistencia_resource = AsistenciaResource()


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^acercade$", TemplateView.as_view(template_name="about.html"), name="about"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^accounts/", include("account.urls")),
    url(r"^clientes/", include("clientes.urls")),
    url(r"^asistencias/", include("asistencias.urls")),
    url(r"^profesores/", include("profesores.urls")),
    #url(r"^cursos/", include("cursos.urls")),
    url(r"^facturas/", include("facturas.urls")),
    url(r"^contacto/nuevo/", ContactoCreateView.as_view(), name="contacto_nuevo"),
    url(r"^alumnos/", include("alumnos.urls")),
    url(r"^aulas/", include("aulas.urls")),
    url(r"^clases/", include("clases.urls")),
    #url(r"^contacto/editar/", ContactoCreateView.as_view(),name="contacto_editar"),
    #url(r'^api/', include(parte_resource.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
