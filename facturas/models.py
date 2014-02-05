from django.db import models
from clientes.models import *
# Create your models here.

FORMAS_PAGO = (
    (0, 'Efectivo'),
    (1, 'Transferencia Bancaria'),
    (2, 'Cobro domiciliado'),
    (3, 'Cheque'),
)

class Concepto(models.Model):
    nombre=models.CharField(max_length=100)
    precio=models.FloatField()
    cantidad=models.DecimalField(max_digits=3,decimal_places=0)
    descuento=models.DecimalField(max_digits=4,decimal_places=2)
    total=models.FloatField()

class Factura(models.Model):
    numero = models.CharField(max_length=25)
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente)
    descuento = models.DecimalField(max_digits=2,decimal_places=0,blank=True)
    iva = models.DecimalField(max_digits=2,decimal_places=0,blank=True)
    retencion = models.DecimalField(max_digits=2,decimal_places=0,blank=True)
    forma_pago=models.DecimalField(max_digits=2, decimal_places=0,choices=FORMAS_PAGO)
    pagada = models.BooleanField()
    conceptos = models.ManyToManyField(Concepto)
    notas = models.TextField(blank=True)
    owner=models.ForeignKey(User)
    def __unicode__(self):
        return "%s - %s" % (self.numero,self.cliente.nombre)
    def calcular_total(self):
        total = 0
        for concepto in self.conceptos:
            total =+ concepto.precio * concepto.cantidad*(1-concepto.descuento/100)
        total = total * (1+self.iva/100)
        return 100
