from django.shortcuts import render
from sales.models import Sale
from sales.forms import SaleForm, SaleFilter
from sales import tables, filters
from payments.models import Payment
from invoices.models import Invoice
from utilities.views import ObjectEditView, ObjectListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
import customers


class SaleEditView(ObjectEditView):
    model = Sale
    form_class = SaleForm
    success_url = reverse_lazy('sale_list')
    template_name = 'sales/add.html'
    cancel_url = 'sale_list'

    def get_object(self, kwargs, request):
        return get_object_or_404(self.model, pk=kwargs['pk'])


class SaleListView(ObjectListView):
    queryset = Sale.objects.select_related('customer').order_by('-id')
    table = tables.SaleTable
    template_name = 'sales/list.html'
    filter = filters.SaleFilter
    filter_form = SaleFilter

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.all()


class SaleListPendingInvoice(SaleListView):
    queryset = Invoice.sales_pending()\
            .select_related('customer').order_by('-id')
    template_name = 'sales/pending_invoice.html'


class SaleListPendingPayment(SaleListView):
    queryset = Payment.sales_pending().\
            select_related('customer').order_by('-id')
    template_name = 'sales/pending_payment.html'


class SaleAddToCustomer(ObjectEditView):
    form_class = SaleForm
    template_name = 'sales/add_sale_customer.html'
    success_url = reverse_lazy('sale_list')
    cancel_url = 'sale_list'
    model = Sale

    def get(self, request, *args, **kwargs):
        customer = get_object_or_404(customers.models.Customer,
                                     pk=kwargs['customer_id'])
        obj = None
        self.success_url = "/customers/{}/".format(customer.id)

        form = self.form_class(
            {'customer': customer})

        return render(request, self.template_name, {
            'obj': obj,
            'customer': customer,
            'obj_type': self.model._meta.verbose_name,
            'form': form,
            'cancel_url': customer.get_absolute_url() if hasattr(customer, 'get_absolute_url') else reverse(self.cancel_url),  # noqa
        })

    def post(self, request, *args, **kwargs):
        self.success_url = "/customers/{}/".format(kwargs['customer_id'])
        return super(SaleAddToCustomer, self).post(request, args, None)


def sale(request, pk):
    queryset = Sale.objects.all()
    sale = get_object_or_404(queryset, pk=pk)
    return render(request, 'sales/show.html', {
        'sale': sale,
    })
