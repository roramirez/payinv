from django.forms import ModelForm, DateField, DateInput
from sales.models import Sale
from utilities.forms import BootstrapMixin


class SaleForm(ModelForm, BootstrapMixin):

    done_at = DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Sale
        fields = ['internal_id', 'customer', 'total_value', 'done_at',
                  'concept', 'notes']


class SaleFilter(ModelForm, BootstrapMixin):
    class Meta:
        model = Sale
        fields = ['customer']
