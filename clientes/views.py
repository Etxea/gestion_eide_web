# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy

from forms import *
from models import *
    
class ClienteCreateView(CreateView):
    model=Cliente   
    form_class = ClienteForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClienteCreateView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse("cliente_lista")
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['accion'] = "crear"
        return context

class ClienteUpdateView(UpdateView):
    model=Cliente
    form_class = ClienteForm   
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClienteUpdateView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse("cliente_lista")
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['accion'] = "editar"
        return context
        
class ClienteDetailView(DetailView):
    model=Cliente
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClienteDetailView, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClienteDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['contacto_form'] = ClienteContactoForm()
        return context

def add_clientet(request):
    form = ClienteForm()
    contacto_formset = ClienteContactoFormset(instance=Pet())
   
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            contacto_formset = ClienteContactoFormset(request.POST, instance=cliente)
            if contacto_formset.is_valid():
                contacto_formset.save()
                return HttpResponseRedirect(reverse('cliente_lista'))
   
    return render(request, "form.html", {
        'form': form,
        'img_formset': img_formset,
        'action': "Create"
    })


class ClienteContactoCreateView(CreateView):
    model=ClienteContacto   
    form_class = ClienteContactoForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ClienteContactoCreateView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        #return reverse_lazy("cliente_detalle",self.object.id)
        #return reverse_lazy("cliente_lista")
        return reverse_lazy("cliente_detalle", kwargs={'pk': self.object.cliente.id})
    def form_valid(self, form):
        cliente = Cliente.objects.get(id=self.kwargs['cliente_id'])
        print "Anadimos el cliente",cliente.nombre
        self.object = form.save(commit=False)
        self.object.cliente = cliente
        self.object.save()
        print "Contacto anadido"
        return super(ClienteContactoCreateView, self).form_valid(form)

class ClienteContactoDeleteView(DeleteView):
    model=ClienteContacto 
    def get_success_url(self):
        return reverse_lazy("cliente_detalle", kwargs={'pk': self.object.cliente.id})
