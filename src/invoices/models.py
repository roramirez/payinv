from django.db import models
from utilities.models import DateTimedModel
from sales.models import Sale
from django.utils.translation import ugettext as _
from django.db.models import OuterRef, Subquery, Sum, Q
from django.db.models.functions import Coalesce


class Invoice(DateTimedModel):
    internal_id = models.CharField(max_length=100)
    sale = models.ForeignKey(Sale)
    total_value = models.DecimalField(
        u'Total Value', default=0, null=True,
        max_digits=10, decimal_places=3)

    date_to_pay = models.DateField()
    date_issue = models.DateField()

    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Invoice')

    def __unicode__(self):
        return "{}".format(self.internal_id)

    def __str__(self):
        return "{}".format(self.internal_id)

    def __get_sales_pending(customer=None):
        invoices = Invoice.objects.filter(sale=OuterRef('pk')).values('sale')
        sum_invoices = invoices.annotate(
            sum=Coalesce(Sum('total_value'), 0)).values('sum')

        q_filter = Q(total_value__gt=Coalesce(Subquery(sum_invoices), 0))
        if customer:
            q_filter &= Q(customer=customer)

        return Sale.objects.filter(q_filter)

    @staticmethod
    def sales_pending_by_customer(customer):
        return Invoice.__get_sales_pending(customer)

    @staticmethod
    def sales_pending():
        return Invoice.__get_sales_pending()
