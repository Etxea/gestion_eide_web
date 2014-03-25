from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

from horas.api import ParteResource

parte_resource = ParteResource()


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^acercade$", TemplateView.as_view(template_name="about.html"), name="about"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^accounts/", include("account.urls")),
    url(r"^clientes/", include("clientes.urls")),
    url(r"^horas/", include("horas.urls")),
    url(r'^api/', include(parte_resource.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
