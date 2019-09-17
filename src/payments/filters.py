import django_filters
from django.db.models import Q
from payments.models import Payment


class PaymentFilter(django_filters.FilterSet):
    q = django_filters.Filter(
        method='search',
        label='Search',
    )

    class Meta:
        model = Payment
        fields = ['total_value']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(total_value__icontains=value)
        )
