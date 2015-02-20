from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from models import *

class ListaAulas(ListView):
    model = Aula
    template_name="aulas.html"
    context_object_name = "aulas_list"
   
class NuevaAula(CreateView):
	model = Aula
	template_name="aula_nueva.html"
	success_url = '/aulas/' ## FIXME esto deberia ser un reverse
	
class EditarAula(UpdateView):
	model = Aula
	template_name="aula_editar.html"
	success_url = "/aulas/"
