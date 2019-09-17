from django.forms import ModelForm
from customers.models import Customer
from utilities.forms import BootstrapMixin


class CustomerForm(ModelForm, BootstrapMixin):
    class Meta:
        model = Customer
        fields = ['name', 'cid', 'address', 'active']
