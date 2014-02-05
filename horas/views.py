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

class ParteLista(ListView):
    model=Parte
    

class ParteNuevo(CreateView):
    model = Parte

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
