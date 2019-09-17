from django.shortcuts import render
from invoices.models import Invoice
from invoices.forms import InvoiceForm
from invoices import tables, filters
from utilities.views import ObjectEditView, ObjectListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404


class InvoiceEditView(ObjectEditView):
    model = Invoice
    form_class = InvoiceForm
    success_url = reverse_lazy('invoice_list')
    template_name = 'invoices/add.html'
    cancel_url = 'invoice_list'

    def get_object(self, kwargs, request):
        return get_object_or_404(self.model, pk=kwargs['pk'])


class InvoiceListView(ObjectListView):
    queryset = Invoice.objects.order_by('-id')
    table = tables.InvoiceTable
    template_name = 'invoices/list.html'
    filter = filters.InvoiceFilter

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.all()


def invoice(request, pk):
    queryset = Invoice.objects.all()
    invoice = get_object_or_404(queryset, pk=pk)
    return render(request, 'invoices/show.html', {
        'invoice': invoice,
    })



