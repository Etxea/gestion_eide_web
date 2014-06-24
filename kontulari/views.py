# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy

from forms import *
from models import *
    
class ContactoCreateView(CreateView):
    model = Contacto   
    form_class = ContactoForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactoCreateView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        if (len(self.object.empresa.all()) > 0):
            return reverse_lazy("cliente_detalle",self.object.empresa.all()[0].id)
            
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContactoCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['accion'] = "crear"
        return context
