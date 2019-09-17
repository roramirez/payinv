import django_filters
from django.db.models import Q
from customers.models import Customer


class CustomerFilter(django_filters.FilterSet):
    q = django_filters.Filter(
        method='search',
        label='Search',
    )

    class Meta:
        model = Customer
        fields = ['name']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value)
        )
