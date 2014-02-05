# Create your views here.
from django.views.generic import DetailView
from books.models import Publisher, Book

class FacturaDetailView(DetailView):

    context_object_name = "factura"
    model = Factura

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FacturaDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['conceptos_list'] = Conceptos.objects.all()
        return context
