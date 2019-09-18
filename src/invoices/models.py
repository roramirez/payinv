from django.db import models
from utilities.models import DateTimedModel
from sales.models import Sale
from django.utils.translation import ugettext as _
from django.db.models import OuterRef, Subquery


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
        return Sale.objects.filter(
            total_value__gt=Subquery(
                Invoice.objects.filter(sale=OuterRef('id')
                                       ).values('total_value').all()
            ))
