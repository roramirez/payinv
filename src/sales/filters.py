import django_filters
from django.db.models import Q
from sales.models import Sale


class SaleFilter(django_filters.FilterSet):
    q = django_filters.Filter(
        method='search',
        label='Search',
    )

    class Meta:
        model = Sale
        fields = ['internal_id']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(internal_id__icontains=value)
        )
