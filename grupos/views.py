from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from models import *
from forms import *


class GrupoListView(ListView):
    model=Grupo
    paginate_by = 50

class GrupoCreateView(CreateView):
    form_class = GrupoCreateForm
    template_name = "grupos/object_form.html"

    def get_success_url(self):
        return reverse_lazy("grupo_lista")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GrupoCreateView, self).dispatch(*args, **kwargs)
class GrupoDetailView(DetailView):
    model = Grupo
    template_name = "grupos/object_detail.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GrupoDetailView, self).dispatch(*args, **kwargs)

class GrupoDeleteView(DeleteView):
    model = Grupo
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GrupoDeleteView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse_lazy("grupos_lista")

class GrupoUpdateView(UpdateView):
    model = Grupo
    form_class = GrupoCreateForm
    template_name = "grupos/object_update_form.html"

    def get_success_url(self):
        return reverse_lazy("grupos_lista")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(GrupoUpdateView, self).dispatch(*args, **kwargs)


