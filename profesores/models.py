from django.db import models
from django.contrib.auth.models import User


class Profesor(models.Model):
    user = models.OneToOneField(User)
    telefono = models.CharField(max_length=9,default="")
    def __unicode__(self):
        return "%s %s (%s)"%(self.user.get_short_name(),self.user.last_name,self.user.username)

    def get_absolute_url(self):
        return "/profesores/%s/"%self.id

    def get_horas_pendientes(self):
        pendiente_horas = 0
        pendiente_minutos = 0
        try:
            horas = self.user.asistencia_set.filter(contabilizado=False).aggregate(Sum('duracion'))
        except:
            print "No podemos agregar fecha asi que a mano"
            for p in self.user.asistencia_set.filter(contabilizado=False):
                print "Sumamos ",p.duracion
                pendiente_horas = pendiente_horas + p.duracion.hour
                pendiente_minutos = pendiente_minutos + p.duracion.minute
        print "Tenemos %s:%s"%(pendiente_horas,pendiente_minutos)
        pendiente_horas = pendiente_horas + pendiente_minutos/60
        pendiente_minutos = pendiente_minutos%60
        print "Tenemos %s:%s"%(pendiente_horas,pendiente_minutos)
        return "%s:%s"%(pendiente_horas,pendiente_minutos)
        


