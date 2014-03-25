from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from horas.models import *


class ParteResource(ModelResource):
    class Meta:
        queryset = Parte.objects.all()
        resource_name = 'parte'
        authentication = BasicAuthentication()
