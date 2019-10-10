from django.forms import ModelForm, CharField, TextInput
from sales.models import Sale
from utilities.forms import BootstrapMixin


class SaleForm(ModelForm, BootstrapMixin):

    done_at = CharField(widget=TextInput(attrs={"class": "datepicker",
                                                "placeholder": ""}))

    class Meta:
        model = Sale
        fields = ['internal_id', 'customer', 'total_value', 'done_at',
                  'concept', 'notes']


class SaleFilter(ModelForm, BootstrapMixin):
    class Meta:
        model = Sale
        fields = ['customer']
