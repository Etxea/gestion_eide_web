from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeletionMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy

from models import *
from forms import *



login_required(ListView.as_view(model=Curso))
class CursosListView(ListView):
    model=Curso
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CursosListView, self).dispatch(*args, **kwargs)

class CursoDetailView(DetailView):
    model = Curso
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CursoDetailView, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CursoDetailView, self).get_context_data(**kwargs)
        # Add extra...
        data = {'curso': self.object.id}
        context['clase_form'] = ClaseForm(initial=data)
        return context

class CursoDeleteView(DeleteView):
    model = Curso
    def get_success_url(self):
        return reverse_lazy("cursos_lista")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CursoDeleteView, self).dispatch(*args, **kwargs)


class ClaseCreateView(CreateView):
    model = Clase
    form_class = ClaseForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClaseCursoCreateView, self).dispatch(*args, **kwargs)


class ClaseDeleteView(DeleteView):
    model = Clase
    def get_success_url(self):
        return reverse_lazy("curso_detalle", kwargs={'pk': self.object.curso.pk})

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClaseDeleteView, self).dispatch(*args, **kwargs)


class ClaseCursoCreateView(ClaseCreateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClaseCursoCreateView, self).dispatch(*args, **kwargs)
    ##Recogemos los datos iniciales (clientes)
    def get_initial(self):
        super(ClaseCursoCreateView, self).get_initial()
        cliente = Cliente.objects.get(pk=self.kwargs['cliente_id'])
        user = self.request.user
        self.initial = {"cliente":cliente.id}
        return self.initial




