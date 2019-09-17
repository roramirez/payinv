import django_filters
from django.db.models import Q
from payments.models import Payment
from sales.models import Sale


class PaymentFilter(django_filters.FilterSet):
    q = django_filters.Filter(
        method='search',
        label='Search',
    )


    sale = django_filters.ModelMultipleChoiceFilter(
            field_name='sale',
            queryset=Sale.objects.all(),
            to_field_name='id',
            label='Sale (id)',
            )



    class Meta:
        model = Payment
        fields = ['total_value']

    def search(self, queryset, name, value):
        return queryset.filter(
            Q(total_value__icontains=value)
        )
