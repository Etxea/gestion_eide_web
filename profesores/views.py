from django.views.generic.edit import CreateView, UpdateView
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
