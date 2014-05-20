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


from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Cliente(models.Model):
    ##user = models.OneToOneField(User,blank=True)
    nombre=models.CharField(max_length=100)
    razon_social=models.CharField(max_length=250)
    NIF=models.CharField(max_length=100)
    direccion=models.CharField(max_length=200)
    telefono = models.CharField(max_length=12,blank=True)
    #web = models.URLField(blank=True)
    #descuento=models.DecimalField(max_digits=4,decimal_places=2,blank=True)
    #notas=models.CharField(max_length=500, blank=True)
    #owner=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombre
    def get_absolute_url(self):
        return "/clientes/%s/"%self.id

    def get_horas_mes(self,ano,mes):
        print "Sumamos las horas del cliente %s en el %s/5s"%(self.nombre,mes,ano)
        pendiente_horas = 0
        pendiente_minutos = 0
        for p in self.parte_set.filter(contabilizado=False):
            print "Sumamos ",p.duracion
            pendiente_horas = pendiente_horas + p.duracion.hour
            pendiente_minutos = pendiente_minutos + p.duracion.minute
        print "Tenemos %s:%s"%(pendiente_horas,pendiente_minutos)
        pendiente_horas = pendiente_horas + pendiente_minutos/60
        pendiente_minutos = pendiente_minutos%60
        print "Tenemos %s:%s"%(pendiente_horas,pendiente_minutos)
        return "%s:%s"%(pendiente_horas,pendiente_minutos)
        
    def get_horas_pendientes(self):
        print "Sumamos las horas del cliente %s"%self.nombre
        pendiente_horas = 0
        pendiente_minutos = 0
        #try:
        #    horas = self.parte_set.filter(contabilizado=False).aggregate(Sum('duracion'))
        #except:
        print "No podemos agregar fecha asi que a mano"
        for p in self.parte_set.filter(contabilizado=False):
            print "Sumamos ",p.duracion
            pendiente_horas = pendiente_horas + p.duracion.hour
            pendiente_minutos = pendiente_minutos + p.duracion.minute
        print "Tenemos %s:%s"%(pendiente_horas,pendiente_minutos)
        pendiente_horas = pendiente_horas + pendiente_minutos/60
        pendiente_minutos = pendiente_minutos%60
        print "Tenemos %s:%s"%(pendiente_horas,pendiente_minutos)
        return "%s:%s"%(pendiente_horas,pendiente_minutos)
