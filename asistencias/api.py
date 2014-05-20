from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from horas.models import *


class AsistenciaResource(ModelResource):
    class Meta:
        queryset = Asistencia.objects.all()
        resource_name = 'Asistencia'
        authentication = BasicAuthentication()
