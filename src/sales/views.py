from django.shortcuts import render
from sales.models import Sale
from sales.forms import SaleForm, SaleFilter
from sales import tables, filters
from payments.models import Payment
from invoices.models import Invoice
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
    filter_form = SaleFilter

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.all()


class SaleListPendingInvoice(SaleListView):
    queryset = Invoice.sales_pending().order_by('-id')
    template_name = 'sales/pending_invoice.html'


class SaleListPendingPayment(SaleListView):
    queryset = Payment.sales_pending().order_by('-id')
    template_name = 'sales/pending_payment.html'


def sale(request, pk):
    queryset = Sale.objects.all()
    sale = get_object_or_404(queryset, pk=pk)
    return render(request, 'sales/show.html', {
        'sale': sale,
    })



