from django.forms import ModelForm, DateField, DateInput
from invoices.models import Invoice
from utilities.forms import BootstrapMixin


class InvoiceForm(ModelForm, BootstrapMixin):

    date_to_pay = DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Invoice
        fields = ['internal_id', 'sale', 'total_value', 'date_to_pay',
                  'notes']
