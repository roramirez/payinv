from django.db import models
from utilities.models import DateTimedModel
from customers.models import Customer
from django.db.models import Sum
from django.utils.translation import ugettext as _
from utilities.utils import csv_format
from django.urls import reverse


class Sale(DateTimedModel):
    internal_id = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer)
    total_value = models.DecimalField(
        u'Total Value', default=0, null=True,
        max_digits=10, decimal_places=3)

    done_at = models.DateField()
    concept = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "{} / {} ".format(self.internal_id, self.customer)

    def __str__(self):
        return "{} / {} ".format(self.internal_id, self.customer)

    def to_csv(self):
        return csv_format([
            self.internal_id,
            self.customer,
            self.total_value,
            self.done_at,
            self.notes,
            self.total_invoices,
            self.total_payments
        ])

    class Meta:
        verbose_name = _('Sale')

    def get_absolute_url(self):
        return reverse('sale', args=[self.pk])

    @property
    def total_payments(self):
        return self.payment_set.all().aggregate(
            Sum('total_value'))['total_value__sum'] or 0

    @property
    def total_invoices(self):
        return self.invoice_set.all().aggregate(
            Sum('total_value'))['total_value__sum'] or 0
