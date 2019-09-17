from django.forms import ModelForm
from sales.models import Sale
from utilities.forms import BootstrapMixin


class SaleForm(ModelForm, BootstrapMixin):
    class Meta:
        model = Sale
        fields = ['internal_id', 'customer', 'total_value', 'done_at',
                  'concept', 'notes']
