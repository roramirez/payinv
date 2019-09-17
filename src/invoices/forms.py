from django.forms import ModelForm
from invoices.models import Invoice
from utilities.forms import BootstrapMixin


class InvoiceForm(ModelForm, BootstrapMixin):
    class Meta:
        model = Invoice
        fields = ['internal_id', 'sale', 'total_value', 'date_to_pay',
                  'notes']
