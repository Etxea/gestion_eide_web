# Create your views here.
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from models import *
from forms import *
from django.forms.models import inlineformset_factory

##FIXME hacer que esto este protegido
def factura_confirmar(request,factura_id):
    #factura = get_object_or_404(Factura, pk=factura_id)
    factura = Factura.objects.get(id=factura_id)
    factura.borrador = False
    factura.save()
    return redirect(factura)
    
    

class FacturaListView(ListView):
    model = Factura
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FacturaListView, self).dispatch(*args, **kwargs)

class FacturaDeleteView(DeleteView):
    model = Factura
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FacturaDeleteView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse_lazy("facturas_lista")

class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaCreateForm
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FacturaCreateView, self).dispatch(*args, **kwargs)

    def get_initial(self):
        super(FacturaCreateView, self).get_initial()
        user = self.request.user
        #Intetamos generar el numero
        numero = "XXXXXXX"
        try:
            last_number = int(Factura.objects.last().numero)
            numero = last_number +1
        except:
            pass
        self.initial = {"owner":user.id,"iva":settings.EMPRESA["IVA"],"numero": numero}
        print self.initial
        return self.initial

class FacturaUpdateView(UpdateView):
    model = Factura
    form_class = FacturaUpdateForm
    template_name = "facturas/factura_update_form.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FacturaUpdateView, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(FacturaUpdateView, self).get_context_data(**kwargs)
        context['empresa'] = settings.EMPRESA
        context['concepto_form'] = ConceptoForm(initial={"factura": self.object.id})
        return context

class FacturaDetailView(DetailView):
    context_object_name = "factura"
    model = Factura
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FacturaDetailView, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FacturaDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context['empresa'] = settings.EMPRESA

        return context

class FacturaImprimir(DetailView):
    context_object_name = "factura"
    model = Factura
    template_name = "facturas/imprimir.html"
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FacturaImprimir, self).dispatch(*args, **kwargs)
    #def get_context_data(self, **kwargs):
    #    # Call the base implementation first to get a context
    #    context = super(FacturaDetailView, self).get_context_data(**kwargs)
    #    # Add in a QuerySet of all the books
    #    context['conceptos_list'] = Conceptos.objects.all()
    #    return context

class ConceptoCreateView(CreateView):
    model = Concepto
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ConceptoCreateView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse_lazy("factura_editar", kwargs = {'pk' : self.object.factura.id, })
    
    def get_initial(self):
        super(ConceptoCreateView, self).get_initial()
        self.initial = {"factura":self.kwargs['factura_id']}
        return self.initial
        
    def form_valid(self, form):
        factura = Factura.objects.get(id=self.kwargs['factura_id'])
        self.object = form.save(commit=False)
        self.object.factura = factura
        self.object.save()
        print "Concepto anadido a factura",self.kwargs['factura_id']
        return super(ConceptoCreateView, self).form_valid(form)

class ConceptoDeleteView(DeleteView):
    model = Concepto
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ConceptoDeleteView, self).dispatch(*args, **kwargs)
    def get_success_url(self):
        return reverse_lazy("factura_editar", kwargs = {'pk' : self.object.factura.id, })
    #OJO sin confirmacion!
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
