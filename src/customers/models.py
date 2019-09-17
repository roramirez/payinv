from django.db import models
from utilities.utils import csv_format
from utilities.models import DateTimedModel


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




    def to_csv(self):
        return csv_format([
            self.name,
            self.cid,
            self.address,
        ])
