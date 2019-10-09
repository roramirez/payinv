from django.forms import ModelForm, ModelChoiceField, CharField, TextInput
from payments.models import Payment
from utilities.forms import BootstrapMixin
import customers
import sales


class PaymentForm(ModelForm, BootstrapMixin):

    pay_at = CharField(widget=TextInput(attrs={"class": "datepicker",
                                               "placeholder": ""}))

    class Meta:
        model = Payment
        fields = ['sale', 'total_value', 'pay_at', 'notes']


class PaymentFilterForm(ModelForm, BootstrapMixin):

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
        model = Payment
        fields = ['sale', 'customer']
