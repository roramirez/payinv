import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable
from invoices.models import Invoice
from django.utils.translation import ugettext as _


class InvoiceTable(BaseTable):
    internal_id = tables.LinkColumn('sale', args=[Accessor('pk')],
                             verbose_name=_('Internal Id'))

    sale = tables.LinkColumn('sale', args=[Accessor('pk')],
                             verbose_name=_('Sale'))

    total_value = tables.Column(verbose_name=_('Total Value'))
    date_to_pay = tables.Column(verbose_name=_('Date to Pay'))

    class Meta(BaseTable.Meta):
        model = Invoice
        fields = ('internal_id', 'sale', 'total_value', 'date_to_pay' )
