from django.db import models

class Aula(models.Model):
    nombre = models.CharField('Nombre',max_length=255,)
    aforo = models.DecimalField(max_digits=3, decimal_places=0)
    pdi = models.BooleanField(default=False,blank=True)
    def __unicode__(self):
         return "%s"%(self.nombre)
    def get_absolute_url(self):
        return "/aulas/editar/%i/" % self.id
