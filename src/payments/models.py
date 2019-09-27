from django.db import models
from utilities.models import DateTimedModel
from sales.models import Sale
from django.utils.translation import ugettext as _
from django.db.models import OuterRef, Subquery, Sum, Q
from django.db.models.functions import Coalesce


class Payment(DateTimedModel):
    sale = models.ForeignKey(Sale)
    total_value = models.DecimalField(
        u'Total Value', default=0, null=True,
        max_digits=10, decimal_places=3)

    pay_at = models.DateField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Payment')

    def __str__(self):
        return "{}".format(self.id)

    def __get_sales_pending(customer=None):
        payments = Payment.objects.filter(sale=OuterRef('pk')).values('sale')
        sum_payments = payments.annotate(
            sum=Coalesce(Sum('total_value'), 0)).values('sum')

        q_filter = Q(total_value__gt=Coalesce(Subquery(sum_payments), 0))
        if customer:
            q_filter &= Q(customer=customer)

        return Sale.objects.filter(q_filter)

    @staticmethod
    def sales_pending_by_customer(customer):
        return Payment.__get_sales_pending(customer)

    @staticmethod
    def sales_pending():
        return Payment.__get_sales_pending()
