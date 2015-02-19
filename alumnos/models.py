from django.db import models
from django.contrib.auth.models import User


class Alumno(models.Model):
    user = models.OneToOneField(User)
    telefono1 = models.CharField(max_length=9,default="")
    telefono2 = models.CharField(max_length=9,default="")
    def __unicode__(self):
        return "%s %s (%s)"%(self.user.get_short_name(),self.user.last_name,self.user.username)

    def get_absolute_url(self):
        return "/alumno/%s/"%self.id