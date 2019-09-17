import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable
from payments.models import Payment
from django.utils.translation import ugettext as _


class PaymentTable(BaseTable):

    sale = tables.LinkColumn('sale', args=[Accessor('pk')],
                             verbose_name=_('Sale'))

    total_value = tables.Column(verbose_name=_('Total Value'))
    pay_at = tables.Column(verbose_name=_('Pay date'))

    class Meta(BaseTable.Meta):
        model = Payment
        fields = ('sale', 'total_value', 'pay_at')
