from django.shortcuts import render
from customers.models import Customer
from customers.forms import CustomerForm
from customers import tables, filters
from utilities.views import ObjectEditView, ObjectListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404


class CustomerEditView(ObjectEditView):
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')
    template_name = 'customers/add.html'
    cancel_url = 'customer_list'

    def get_object(self, kwargs, request):
        return get_object_or_404(self.model, pk=kwargs['pk'])


class CustomerListView(ObjectListView):
    queryset = Customer.objects.order_by('-id')
    table = tables.CustomerTable
    template_name = 'customers/list.html'
    filter = filters.CustomerFilter

    # Hook filter by request
    def alter_queryset(self, request):
        return self.queryset.all()


def customer(request, pk):
    queryset = Customer.objects.all()
    customer = get_object_or_404(queryset, pk=pk)
    return render(request, 'customers/show.html', {
        'customer': customer,
    })



