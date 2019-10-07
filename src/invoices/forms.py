from django.forms import ModelForm, DateField, DateInput, ModelChoiceField
from invoices.models import Invoice
from utilities.forms import BootstrapMixin
import customers
import sales


class InvoiceForm(ModelForm, BootstrapMixin):

    date_to_pay = DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Invoice
        fields = ['internal_id', 'sale', 'total_value', 'date_to_pay',
                  'notes', 'date_issue']


class InvoiceFilterForm(ModelForm, BootstrapMixin):

    sale = ModelChoiceField(
        queryset=sales.models.Sale.objects.all(),
        required=False)

    customer = ModelChoiceField(
        queryset=customers.models.Customer.objects.all(),
        required=False,
        to_field_name='id',
        help_text='Invoices for a Customer',
        error_messages={
            'invalid_choice': 'Customer not found.',
        }
    )

    class Meta:
        model = Invoice
        fields = ['sale', 'date_issue', 'customer']
