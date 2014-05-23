from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from clientes.models import *

# Create your models here.

FORMAS_PAGO = (
    (0, 'Efectivo'),
    (1, 'Transferencia Bancaria'),
    (2, 'Cobro domiciliado'),
    (3, 'Cheque'),
)
IVA = (
    (0, 'Exento'),
    (10, 'Supereducido'),
    (14, 'Reducido'),
    (21, 'Normal'),
)

class Factura(models.Model):
    numero = models.CharField(max_length=25)
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente)
    descuento = models.DecimalField(max_digits=2,decimal_places=0,default=0)
    iva = models.DecimalField(max_digits=2,decimal_places=0,blank=True,choices=IVA,default=settings.EMPRESA["IVA"])
    retencion = models.DecimalField(max_digits=2,decimal_places=0,default=settings.EMPRESA["RETENCION"])
    forma_pago=models.DecimalField(max_digits=2, decimal_places=0,choices=FORMAS_PAGO,default=settings.EMPRESA["FORMA_PAGO"])
    borrador = models.BooleanField(default=True)
    pagada = models.BooleanField(default=False)
    notas = models.TextField(blank=True)
    owner=models.ForeignKey(User)
    subtotal = models.FloatField(default=0)
    total=models.FloatField(default=0)
    def get_absolute_url(self):
        if self.borrador:
            return reverse_lazy("factura_editar", kwargs = {'pk' : self.id, })
        else:
            return reverse_lazy("factura_detalle", kwargs = {'pk' : self.id, })

    def __unicode__(self):
        return "%s - %s" % (self.numero,self.cliente.nombre)
    def calcula_subtotal(self):
        subtotal=0
        for concepto in self.concepto_set.all():
            print "Sumando concepto ",concepto.nombre,concepto.total
            subtotal = subtotal + concepto.total
        print "Subtotal",subtotal
        self.subtotal = subtotal
        return subtotal
    def calcular_total(self):
        total = float(0)
        self.calcula_subtotal()
        total = float(self.subtotal)*(1+float(self.iva)/100)
        self.total = total
        return total
    def save(self, *args, **kwargs):
        self.calcular_total()
        super(Factura, self).save(*args, **kwargs)

class Concepto(models.Model):
    factura = models.ForeignKey(Factura)
    nombre=models.CharField(max_length=100)
    precio=models.FloatField()
    cantidad=models.DecimalField(max_digits=3,decimal_places=0,default=1)
    descuento=models.DecimalField(max_digits=4,decimal_places=2,default=0.0)
    total=models.FloatField(default=0)
    def calcular_total(self):
        total = self.precio*float(self.cantidad)
        total = total*(100-float(self.descuento))/100
        self.total = total
    def save(self, *args, **kwargs):
        self.calcular_total()
        super(Concepto, self).save(*args, **kwargs)
        factura = Factura.objects.get(id=self.factura_id)
        factura.calcular_total()
        factura.save()
    def delete(self, *args, **kwargs):
        super(Concepto, self).delete(*args, **kwargs)
        factura = Factura.objects.get(id=self.factura_id)
        factura.calcular_total()
        factura.save()

