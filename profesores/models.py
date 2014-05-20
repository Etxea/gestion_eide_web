from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):  
    user = models.OneToOneField(User)
    def __unicode__(self):
        return "%s %s (%s)"%(self.user.get_short_name(),self.user.last_name,self.user.username)
        
    def get_absolute_url(self):
        return "/profesores/%s/"%self.id
    
    
