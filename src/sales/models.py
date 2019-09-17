from django.db import models
from utilities.utils import csv_format
from utilities.models import DateTimedModel
from customers.models import Customer

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
        return "{}".format(self.internal_id)

    def __str__(self):
        return "{}".format(self.internal_id)

