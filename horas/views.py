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
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import get_object_or_404

class ParteLista(ListView):
    model=Parte
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ParteLista, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lista_clientes'] = Cliente.objects.all()
        return context

class ParteListaCliente(ParteLista):
    def get_queryset(self):
        cliente = get_object_or_404(Cliente, pk=self.kwargs['cliente_id'])
        return Parte.objects.filter(cliente=cliente)    

class ParteNuevo(CreateView):
    model = Parte
    def get_initial(self):
        super(ParteNuevo, self).get_initial()
        user = self.request.user
        self.initial = {"usuario":user.id}
        return self.initial

class ParteNuevoCliente(CreateView):
    model = Parte
    ##Recogemos los datos iniciales (clientes y user)
    def get_initial(self):
        super(ParteNuevoCliente, self).get_initial()
        cliente = Cliente.objects.get(pk=self.kwargs['cliente_id'])
        user = self.request.user
        self.initial = {"cliente":cliente.id, "usuario":user.id}
        return self.initial

class ParteEditar(UpdateView):
    model = Parte
