from django.shortcuts import render
from sales.models import Sale
from sales.forms import SaleForm
from sales import tables, filters
from utilities.views import ObjectEditView, ObjectListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404


class SaleEditView(ObjectEditView):
    model = Sale
    form_class = SaleForm
    success_url = reverse_lazy('sale_list')
    template_name = 'sales/add.html'
    cancel_url = 'sale_list'

    def get_object(self, kwargs, request):
        return get_object_or_404(self.model, pk=kwargs['pk'])


class SaleListView(ObjectListView):
    queryset = Sale.objects.order_by('-id')
    table = tables.SaleTable
    template_name = 'sales/list.html'
    filter = filters.SaleFilter

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.all()


def sale(request, pk):
    queryset = Sale.objects.all()
    sale = get_object_or_404(queryset, pk=pk)
    return render(request, 'sales/show.html', {
        'sale': sale,
    })


