from django.db import models
from utilities.models import DateTimedModel
from sales.models import Sale
from django.utils.translation import ugettext as _
from django.db.models import OuterRef, Subquery, Sum
from django.db.models.functions import Coalesce


class Invoice(DateTimedModel):
    internal_id = models.CharField(max_length=100)
    sale = models.ForeignKey(Sale)
    total_value = models.DecimalField(
        u'Total Value', default=0, null=True,
        max_digits=10, decimal_places=3)

    date_to_pay = models.DateField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _('Invoice')

    def __unicode__(self):
        return "{}".format(self.internal_id)

    def __str__(self):
        return "{}".format(self.internal_id)

    @staticmethod
    def sales_pending():
        invoices = Invoice.objects.filter(sale=OuterRef('pk')).values('sale')
        sum_invoices = invoices.annotate(
            sum=Coalesce(Sum('total_value'), 0)).values('sum')
        return Sale.objects.filter(
            total_value__gt=Coalesce(Subquery(sum_invoices), 0))
