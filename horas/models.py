#  models.py
#  
#  Copyright 2014 jon latorre <patataman@schrodinger>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime

from clientes.models import Cliente
TIPO_PARTE = (
    (1, _('Local')),
    (2, _('Remoto'))
)



class Bono(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    
    cliente = models.ForeignKey(Cliente)
    duracion= models.DecimalField(decimal_places=0,max_digits=3)
    owner=models.ForeignKey(User)
    facturado = models.BooleanField(default=False)
    
    def __unicode__(self):
        return "%s - %s"%(self.cliente,self.fecha)
    def get_absolute_url(self):
        return "%s/"%self.id


class Parte(models.Model):
    fecha 		= models.DateField(default=datetime.date.today)
    duracion 	= models.TimeField()
    notas 		= models.CharField(max_length=500, blank=True)
    tipo		= models.DecimalField(decimal_places=0,max_digits=2,choices= TIPO_PARTE)
    cliente		= models.ForeignKey(Cliente)
    usuario		= models.ForeignKey(User, blank=True, null=True)
    def __unicode__(self):
        return self.nombre
    def get_absolute_url(self):
        return "partes/%s/"%self.id


