#  views.py
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

from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

from models import *
from forms import *
from clientes.models import *
from cursos.models import *

class AsistenciaLista(ListView):
    template_name = "asistencias/asistencia_list_completa.html"
    model=Asistencia
    paginate_by = 12
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AsistenciaLista, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AsistenciaLista, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lista_clientes'] = Cliente.objects.all()
        context['lista_cursos'] = Curso.objects.all()
        context['lista_usuarios'] = User.objects.all()
        return context
    def get_queryset(self):
        if self.request.user.is_staff:
            return Asistencia.objects.all().order_by('-fecha')
        else:
            return Asistencia.objects.filter(usuario=self.request.user).order_by('-fecha')

class AsistenciaListaPendientes(AsistenciaLista):
    template_name = "asistencias/asistencia_list.html"
    def get_queryset(self):
        if self.request.user.is_staff:
            return Asistencia.objects.all().filter(contabilizado=False).order_by('-fecha')
        else:
            return Asistencia.objects.filter(usuario=self.request.user).filter(contabilizado=False).order_by('-fecha')

class AsistenciaListaCurso(AsistenciaLista):
    def get_queryset(self):
        curso = get_object_or_404(Curso, pk=self.kwargs['curso_id'])
        return Asistencia.objects.filter(curso=curso).order_by('-fecha')

class AsistenciaListaUsuario(AsistenciaLista):
    def get_queryset(self):
        usuario = get_object_or_404(User, pk=self.kwargs['usuario_id'])
        return Asistencia.objects.filter(usuario=usuario).order_by('-fecha')

class AsistenciaListaCliente(AsistenciaLista):
    def get_queryset(self):
        cliente = get_object_or_404(Cliente, pk=self.kwargs['cliente_id'])
        cursos = Curso.objects.filter(cliente=cliente)
        return Asistencia.objects.filter(curso=cursos).order_by('-fecha')

class MisAsistencias(AsistenciaLista):
    def get_queryset(self):
        return Asistencia.objects.filter(usuario=self.request.user).order_by('-fecha')


class AsistenciaListaFecha(AsistenciaLista):
    template_name = "asistencias/_tabla_asistencias.html"
    
    def get_queryset(self):
        inicio = "%s-%s-%s"%(self.kwargs['inicio_ano'],self.kwargs['inicio_mes'],self.kwargs['inicio_dia'])
        fin = "%s-%s-%s"%(self.kwargs['fin_ano'],self.kwargs['fin_mes'],self.kwargs['fin_dia'])
        print "Listamos las asistencia entra %s y %s"%(inicio,fin)
        return Asistencia.objects.filter(fecha__gte=inicio).filter(fecha__lte=fin).order_by('-fecha')


class AsistenciaNueva(CreateView):
    model = Asistencia
    form_class = AsistenciaForm
    def get_success_url(self):
        return reverse("asistencias_lista")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AsistenciaNueva, self).dispatch(*args, **kwargs)

    def get_initial(self):
        super(AsistenciaNueva, self).get_initial()
        user = self.request.user
        self.initial = {"usuario":user.id}
        return self.initial
    def form_valid(self, form):
        print "hacemos que el usuario sea ",self.request.user
        form.instance.usuario = self.request.user
        return super(AsistenciaNueva, self).form_valid(form)
    def get_context_data(self, **kwargs):
        context = super(AsistenciaNueva, self).get_context_data(**kwargs)
        profesor = Profesor.objects.get(user=self.request.user)
        context['form'].fields['curso'].queryset = Curso.objects.filter(clase=profesor.clase_set.all())
        return context


class AsistenciaNuevaCurso(AsistenciaNueva):
    ##Recogemos los datos iniciales (clientes y user)
    def get_initial(self):
        super(AsistenciaNuevaCurso, self).get_initial()
        curso = Curso.objects.get(pk=self.kwargs['curso_id'])
        user = self.request.user
        self.initial = {"curso":curso.id, "usuario":user.id}
        return self.initial

class AsistenciaEditar(UpdateView):
    model = Asistencia
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AsistenciaEditar, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse("asistencias_lista")

class AsistenciaDetalle(DetailView):
    model = Asistencia
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AsistenciaDetalle, self).dispatch(*args, **kwargs)
