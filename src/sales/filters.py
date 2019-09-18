import django_filters
from django.db.models import Q
from sales.models import Sale
from customers.models import Customer


class SaleFilter(django_filters.FilterSet):
    q = django_filters.Filter(
        method='search',
        label='Search',
    )

    customer = django_filters.ModelMultipleChoiceFilter(
        field_name='customer',
        queryset=Customer.objects.all(),
        to_field_name='id',
        label='Customer (id)',
    )

    class Meta:
        model = Sale
        fields = ['internal_id']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(internal_id__icontains=value)
        )
