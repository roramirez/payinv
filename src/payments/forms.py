from django.forms import ModelForm, DateField, DateInput
from payments.models import Payment
from utilities.forms import BootstrapMixin


class PaymentForm(ModelForm, BootstrapMixin):

    pay_at = DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Payment
        fields = ['sale', 'total_value', 'pay_at', 'notes']
