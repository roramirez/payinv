import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable
from sales.models import Sale
from django.utils.translation import ugettext as _
from django.utils.html import format_html
from django.urls import reverse


class SaleTable(BaseTable):
    internal_id = tables.LinkColumn('sale', args=[Accessor('pk')],
                                    verbose_name=_('Internal Id'))

    customer = tables.LinkColumn('customer', args=[Accessor('pk')],
                                 verbose_name=_('Customer'))

    total_value = tables.Column(verbose_name=_('Total Value'))
    concept = tables.Column(verbose_name=_('Concept'))
    done_at = tables.Column(verbose_name=_('Date'))

    # FIXME: Make me happy. Sort this colums
    total_payments = tables.LinkColumn(verbose_name=_('Total Payments'),
                                       orderable=False)
    total_invoices = tables.LinkColumn(verbose_name=_('Total Invoices'),
                                       orderable=False)

    class Meta(BaseTable.Meta):
        model = Sale
        fields = ('internal_id', 'customer',
                  'concept', 'total_value', 'done_at')

    def render_total_invoices(self, record):
        url = reverse('invoice_list')
        return format_html('<a href="{}?sale={}">{}</a>',
                           url, record.id, record.total_invoices)

    def render_total_payments(self, record):
        url = reverse('payment_list')
        return format_html('<a href="{}?sale={}">{}</a>',
                           url, record.id, record.total_payments)
