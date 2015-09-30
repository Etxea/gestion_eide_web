from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from models import *
from forms import *


class AlumnoListView(ListView):
    model=Alumno
    paginate_by = 50
class AlumnoCreateView(CreateView):
    form_class = AlumnoCreateForm
    template_name = "alumnos/alumno_form.html"

    def get_success_url(self):
        return reverse_lazy("alumnos_lista")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AlumnoCreateView, self).dispatch(*args, **kwargs)
class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = "alumnos/alumno_detail.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AlumnoDetailView, self).dispatch(*args, **kwargs)

class AlumnoDeleteView(DeleteView):
    model = Alumno
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AlumnoDeleteView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse_lazy("alumnos_lista")

class AlumnoUpdateView(UpdateView):
    model = Alumno
    form_class = AlumnoCreateForm
    template_name = "alumnos/alumno_update_form.html"

    def get_success_url(self):
        return reverse_lazy("alumnos_lista")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AlumnoUpdateView, self).dispatch(*args, **kwargs)



class CursoListView(ListView):
    model=Curso
    paginate_by = 50
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CursoListView, self).dispatch(*args, **kwargs)
class CursoCreateView(CreateView):
    form_class = CursoCreateForm
    template_name = "alumnos/curso_form.html"
    def get_success_url(self):
        return reverse_lazy("cursos_lista")
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CursoCreateView, self).dispatch(*args, **kwargs)
class CursoDetailView(DetailView):
    model = Curso
    template_name = "alumnos/curso_detail.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CursoDetailView, self).dispatch(*args, **kwargs)
class CursoDeleteView(DeleteView):
    model = Curso
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CursoDeleteView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse_lazy("cursos_lista")
class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoCreateForm
    template_name = "alumnos/curso_update_form.html"
    def get_success_url(self):
        return reverse_lazy("cursos_lista")
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CursoUpdateView, self).dispatch(*args, **kwargs)
