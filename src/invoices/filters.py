import django_filters
from django.db.models import Q
from invoices.models import Invoice


class InvoiceFilter(django_filters.FilterSet):
    q = django_filters.Filter(
        method='search',
        label='Search',
    )

    class Meta:
        model = Invoice
        fields = ['internal_id']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(internal_id__icontains=value)
        )
