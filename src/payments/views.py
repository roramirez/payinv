from django.shortcuts import render
from payments.models import Payment
from payments.forms import PaymentForm, PaymentFilterForm
from payments import tables, filters
from utilities.views import ObjectEditView, ObjectListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.urls import reverse
import sales


class PaymentEditView(ObjectEditView):
    model = Payment
    form_class = PaymentForm
    success_url = reverse_lazy('payment_list')
    template_name = 'payments/add.html'
    cancel_url = 'payment_list'

    def get_object(self, kwargs, request):
        return get_object_or_404(self.model, pk=kwargs['pk'])


class PaymentAddToSale(ObjectEditView):
    form_class = PaymentForm
    template_name = 'sales/add_payment.html'
    success_url = reverse_lazy('payment_list')
    cancel_url = 'payment_list'
    model = Payment

    def get(self, request, *args, **kwargs):
        sale = get_object_or_404(sales.models.Sale, pk=kwargs['sale_id'])
        obj = None
        self.success_url = "/sales/{}/".format(sale.id)

        form = self.form_class(
            {'total_value': sale.total_value - sale.total_payments,
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
        return super(PaymentAddToSale, self).post(request, args, None)


class PaymentListView(ObjectListView):
    queryset = Payment.objects.select_related('sale').order_by('-id')
    table = tables.PaymentTable
    template_name = 'payments/list.html'
    filter = filters.PaymentFilter
    filter_form = PaymentFilterForm

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.all()


def payment(request, pk):
    queryset = Payment.objects.all()
    payment = get_object_or_404(queryset, pk=pk)
    return render(request, 'payments/show.html', {
        'payment': payment,
    })
