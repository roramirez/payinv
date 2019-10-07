import django_filters
from django.db.models import Q
from invoices.models import Invoice
from sales.models import Sale
import customers


class InvoiceFilter(django_filters.FilterSet):
    q = django_filters.Filter(
        method='search',
        label='Search',
    )

    sale = django_filters.ModelChoiceFilter(
        field_name='sale',
        queryset=Sale.objects.all(),
        to_field_name='id',
        label='Sale (id)',
    )

    customer = django_filters.ModelChoiceFilter(
        queryset=customers.models.Customer.objects.all(),
        field_name='sale__customer_id',
        label='Customer (id)',
    )

    class Meta:
        model = Invoice
        fields = ['internal_id']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(internal_id__icontains=value)
        )
