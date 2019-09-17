from django.forms import ModelForm
from payments.models import Payment
from utilities.forms import BootstrapMixin


class PaymentForm(ModelForm, BootstrapMixin):
    class Meta:
        model = Payment
        fields = ['sale', 'total_value', 'pay_at', 'notes']
