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
        sales_id = self.sale_set.all().values('id')
        return payments.models.Payment.objects.filter(
            sale_id__in=sales_id).aggregate(
            Sum('total_value'))['total_value__sum'] or 0

    @property
    def total_invoices(self):
        sales_id = self.sale_set.all().values('id')
        return invoices.models.Invoice.objects.filter(
            sale_id__in=sales_id).aggregate(
            Sum('total_value'))['total_value__sum'] or 0
