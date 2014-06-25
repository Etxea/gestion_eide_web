from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from models import *
from forms import *



class ProfesorCreateView(CreateView):
    form_class = ProfesorCreateForm
    template_name = "profesores/profesor_form.html"

    def get_success_url(self):
        return reverse_lazy("profesores_lista")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfesorCreateView, self).dispatch(*args, **kwargs)


class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = "profesores/profesor_detail.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfesorDetailView, self).dispatch(*args, **kwargs)

class ProfesorDeleteView(DeleteView):
    model = Profesor
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfesorDeleteView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse_lazy("profesores_lista")

class ProfesorUpdateView(UpdateView):
    model = Profesor
    form_class = ProfesorCreateForm
    template_name = "profesores/profesor_update_form.html"

    def get_success_url(self):
        return reverse_lazy("profesores_lista")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfesorUpdateView, self).dispatch(*args, **kwargs)
