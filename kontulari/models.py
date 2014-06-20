from django.db import models

class Contacto(models.Model):
    nombre=models.CharField(max_length=100)
    email=models.EmailField(blank=True)
    telefono = models.CharField(max_length=12,blank=True)
