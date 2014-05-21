from django.forms.models import inlineformset_factory
FacturaFormset = inlineformset_factory(Factura, Concepto)
