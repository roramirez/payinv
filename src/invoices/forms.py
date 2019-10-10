from django.forms import ModelForm, ModelChoiceField, CharField, TextInput
from invoices.models import Invoice
from utilities.forms import BootstrapMixin
import customers
import sales


class InvoiceForm(ModelForm, BootstrapMixin):

    date_to_pay = CharField(widget=TextInput(attrs={"class": "datepicker",
                                                    "placeholder": ""}))
    date_issue = CharField(widget=TextInput(attrs={"class": "datepicker",
                                                   "placeholder": ""}))

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
