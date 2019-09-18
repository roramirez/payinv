from django.shortcuts import render
from payments.models import Payment
from payments.forms import PaymentForm, PaymentFilterForm
from payments import tables, filters
from utilities.views import ObjectEditView, ObjectListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404


class PaymentEditView(ObjectEditView):
    model = Payment
    form_class = PaymentForm
    success_url = reverse_lazy('payment_list')
    template_name = 'payments/add.html'
    cancel_url = 'payment_list'

    def get_object(self, kwargs, request):
        return get_object_or_404(self.model, pk=kwargs['pk'])


class PaymentListView(ObjectListView):
    queryset = Payment.objects.order_by('-id')
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
