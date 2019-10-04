from django.db import models
from utilities.utils import csv_format
from utilities.models import DateTimedModel
from django.utils.translation import ugettext as _
from django.db.models import Sum
import invoices
import payments


class Customer(DateTimedModel):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    cid = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    post_pay = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Customer')

    def to_csv(self):
        return csv_format([
            self.name,
            self.cid,
            self.address,
        ])

    @property
    def total_sales(self):
        return self.sale_set.all().aggregate(
            Sum('total_value'))['total_value__sum'] or 0

    @property
    def total_payments(self):
        return payments.models.Payment.objects.filter(
            sale__in=self.sale_set.all()).aggregate(
            Sum('total_value'))['total_value__sum'] or 0

    @property
    def total_invoices(self):
        return invoices.models.Invoice.objects.filter(
            sale__in=self.sale_set.all()).aggregate(
            Sum('total_value'))['total_value__sum'] or 0

    @property
    def count_sales_invoices_pending(self):
        return invoices.models.Invoice.sales_pending_by_customer(self).count()

    @property
    def count_sales_payments_pending(self):
        return payments.models.Payment.sales_pending_by_customer(self).count()
