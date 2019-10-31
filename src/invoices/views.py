from django.shortcuts import render
from invoices.models import Invoice
from invoices.forms import InvoiceForm, InvoiceFilterForm
from invoices import tables, filters
from utilities.views import ObjectEditView, ObjectListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
import sales


class InvoiceEditView(ObjectEditView):
    model = Invoice
    form_class = InvoiceForm
    success_url = reverse_lazy('invoice_list')
    template_name = 'invoices/add.html'
    cancel_url = 'invoice_list'

    def get_object(self, kwargs, request):
        return get_object_or_404(self.model, pk=kwargs['pk'])


class InvoiceAddToSale(ObjectEditView):
    form_class = InvoiceForm
    template_name = 'sales/add_invoice.html'
    success_url = reverse_lazy('invoice_list')
    cancel_url = 'invoice_list'
    model = Invoice

    def get(self, request, *args, **kwargs):
        sale = get_object_or_404(sales.models.Sale, pk=kwargs['sale_id'])
        obj = None
        self.success_url = "/sales/{}/".format(sale.id)

        form = self.form_class(
            {'total_value': sale.total_value - sale.total_invoices,
             'sale': sale})

        return render(request, self.template_name, {
            'obj': obj,
            'sale': sale,
            'obj_type': self.model._meta.verbose_name,
            'form': form,
            'cancel_url': sale.get_absolute_url() if hasattr(sale, 'get_absolute_url') else reverse(self.cancel_url),  # noqa
        })

    def post(self, request, *args, **kwargs):
        self.success_url = "/sales/{}/".format(kwargs['sale_id'])
        return super(InvoiceAddToSale, self).post(request, args, None)


class InvoiceListView(ObjectListView):
    queryset = Invoice.objects.select_related('sale').order_by('-id')
    table = tables.InvoiceTable
    template_name = 'invoices/list.html'
    filter = filters.InvoiceFilter
    filter_form = InvoiceFilterForm

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.all()


def invoice(request, pk):
    queryset = Invoice.objects.all()
    invoice = get_object_or_404(queryset, pk=pk)
    return render(request, 'invoices/show.html', {
        'invoice': invoice,
    })
