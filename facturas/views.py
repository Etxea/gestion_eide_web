# Create your views here.
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView,CreateView
from django.core.urlresolvers import reverse_lazy
from models import *
from django.forms.models import inlineformset_factory

class FacturaListView(ListView):
    model = Factura

class FacturaCreateView(CreateView):
    model = Factura
#    FacturaFormset = inlineformset_factory(Factura, Concepto)

class FacturaUpdateView(UpdateView):
    model = Factura

class FacturaDetailView(DetailView):

    context_object_name = "factura"
    model = Factura
    def get_success_url(self):
        return reverse_lazy("cursos_lista")
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FacturaDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['conceptos_list'] = Conceptos.objects.all()
        return context

class FacturaImprimir(DetailView):
    context_object_name = "factura"
    model = Factura
    template_name = "facturas/imprimir.html"
    #def get_context_data(self, **kwargs):
    #    # Call the base implementation first to get a context
    #    context = super(FacturaDetailView, self).get_context_data(**kwargs)
    #    # Add in a QuerySet of all the books
    #    context['conceptos_list'] = Conceptos.objects.all()
    #    return context

class ConceptoCreateView(CreateView):
    model = Concepto
