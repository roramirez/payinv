from django.db import models
from utilities.models import DateTimedModel
from sales.models import Sale
from django.utils.translation import ugettext as _
from django.db.models import OuterRef, Subquery


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

    @staticmethod
    def sales_pending():
        return Sale.objects.filter(
            total_value__gt=Subquery(
                Payment.objects.filter(
                    sale=OuterRef('id')).values('total_value').all()))
