from django.db import models
import datetime
from profesores.models import Profesor
from aulas.models import Aula

class Clase(models.Model):
    nombre = models.CharField('Nombre',max_length=255,)
    aula = models.ForeignKey(Aula,related_name='clases')
    profesor = models.ForeignKey(Profesor,related_name='clases')
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    padre = models.ForeignKey('Clase',related_name='repeticiones',blank=True,null=True) #igual editable=False es interesante??

    def fecha(self):
        return self.hora_inicio.date()
    def fecha_hora(self):
        texto = "%s - %s:%s - %s:%s"%(self.hora_inicio.date(),self.hora_inicio.hour,\
            self.hora_inicio.minute,self.hora_fin.hour,self.hora_fin.minute)
        return texto
    def __unicode__(self):
        return "%s [%s] (%s)"%(self.nombre, self.fecha(),self.aula)    
    def __str__(self):
        return self.__unicode__()
    def get_absolute_url(self):
        return "/clases/editar/%i/" % self.id

    def repetir(self, semanas):
        print "Vamos a anadir repeticiones las siguientes %s semanas"%semanas
        count = 1
        while ( count <= semanas ):
            print "Repeticion %s"%(count)
            count+=1
            repeticion = Clase(nombre=self.nombre, aula=self.aula, profesor=self.profesor,\
            hora_inicio=self.hora_inicio + datetime.timedelta(days=7*count),hora_fin=self.hora_fin + datetime.timedelta(days=7*count),padre=self)
            repeticion.save()
            print repeticion.id
        
def get_clases_dia(fecha,aula=None,profesor=None):
    """funcion que devuelve todas las clases que hay en un dia concreto""" 
    if aula:
        print "Vamos a listar las de aula %s"%aula
        ret = Clase.objects.filter(hora_inicio__gte=fecha,hora_fin__lte=fecha+datetime.timedelta(days=1),aula=aula)
    elif profesor:
        print "Vamos a listar las de prfesort %s"%profesor
        ret = Clase.objects.filter(hora_inicio__gte=fecha,hora_fin__lte=fecha+datetime.timedelta(days=1),profesor=profesor)
    else:
        ret = Clase.objects.filter(hora_inicio__gte=fecha,hora_fin__lte=fecha+datetime.timedelta(days=1))
    print "Encontradas %s clases el dia %s"%(ret.count(),fecha)
    return ret

def get_profesores_libres(hora_incio,hora_fin):
    pass
    
def programacion_profesor_dia(profesor,dia):
    #profesor = Profesor.objects.get(id=id)
    clases = []
    for hora in range(8,22):
        #print "Vamos con la hora %s"%hora
        for cuarto in range(00,60,15):
            fecha_consulta = datetime.datetime(dia.year,dia.month,dia.day,hora,cuarto,0)
            #print "Vamos con la fecha de consulta %s"%(fecha_consulta)
            clase = Clase.objects.filter(profesor=profesor, hora_inicio__lte=fecha_consulta,hora_fin__gte=fecha_consulta)
            if clase.count() == 1:
                clase = clase[0]
                #print "Anadimos la clase es: %s" % clase
                clases.append(["%s:%s"%(hora,cuarto),"%s-%s"%(clase.nombre,clase.aula.nombre)])
            else:
                clases.append(["%s:%s"%(hora,cuarto),""])
    return clases

def programacion_aula_dia(aula,dia):
    #profesor = Profesor.objects.get(id=id)
    clases = []
    for hora in range(8,22):
        #print "Vamos con la hora %s"%hora
        for cuarto in range(00,60,15):
            fecha_consulta = datetime.datetime(dia.year,dia.month,dia.day,hora,cuarto,0)
            #print "Vamos con la fecha de consulta %s"%(fecha_consulta)
            clase = Clase.objects.filter(aula=aula, hora_inicio__lte=fecha_consulta,hora_fin__gte=fecha_consulta)
            if clase.count() == 1:
                clase = clase[0]
                #print "Anadimos la clase es: %s" % clase
                clases.append(["%s:%s"%(hora,cuarto),"%s-%s"%(clase.nombre,clase.aula.nombre)])
            else:
                clases.append(["%s:%s"%(hora,cuarto),"................"])
    return clases
