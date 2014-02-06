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

from models import *
from clientes.models import *
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

class ParteLista(ListView):
    model=Parte
    paginate_by = 12
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParteLista, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ParteLista, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lista_clientes'] = Cliente.objects.all()
        context['lista_usuarios'] = User.objects.all()
        return context

class ParteListaPendientes(ParteLista):
    def get_queryset(self):
        
        return Parte.objects.filter(contabilizado=False)    

class ParteListaCliente(ParteLista):
    def get_queryset(self):
        cliente = get_object_or_404(Cliente, pk=self.kwargs['cliente_id'])
        return Parte.objects.filter(cliente=cliente)    

class ParteListaUsuario(ParteLista):
    def get_queryset(self):
        usuario = get_object_or_404(User, pk=self.kwargs['usuario_id'])
        return Parte.objects.filter(usuario=usuario)    

class MisPartes(ParteLista):
    def get_queryset(self):
        return Parte.objects.filter(usuario=self.request.user)    


class ParteNuevo(CreateView):
    model = Parte
    def get_success_url(self):
        return reverse("partes_lista") 

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParteNuevo, self).dispatch(*args, **kwargs)

    def get_initial(self):
        super(ParteNuevo, self).get_initial()
        user = self.request.user
        self.initial = {"usuario":user.id}
        return self.initial

class ParteNuevoCliente(ParteNuevo):
    ##Recogemos los datos iniciales (clientes y user)
    def get_initial(self):
        super(ParteNuevoCliente, self).get_initial()
        cliente = Cliente.objects.get(pk=self.kwargs['cliente_id'])
        user = self.request.user
        self.initial = {"cliente":cliente.id, "usuario":user.id}
        return self.initial

class ParteEditar(UpdateView):
    model = Parte
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParteEditar, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse("partes_lista") 

class ParteDetalle(DetailView):
    model = Parte
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParteDetalle, self).dispatch(*args, **kwargs)
