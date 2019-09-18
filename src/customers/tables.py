import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable
from customers.models import Customer
from core.utils import yes_or_no
from django.utils.translation import ugettext as _


class CustomerTable(BaseTable):
    name = tables.LinkColumn('customer', args=[Accessor('pk')],
                             verbose_name=_('Name'))
    address = tables.Column(verbose_name=_('Address'))
    active = tables.Column(verbose_name=_('Active'))
    created_at = tables.Column(verbose_name=_('Created At'))

    class Meta(BaseTable.Meta):
        model = Customer
        fields = ('name', 'address', 'active', 'created_at')

    def render_active(self, value):
        return yes_or_no(value)
