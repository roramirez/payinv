from django.shortcuts import render
import customers
import sales
import payments
import invoices
from django.db.models import Count, Sum


def HomePage(request):
    """ home page """

    invoices_pending = invoices.models.Invoice.sales_pending()
    invoices_pending_total = invoices_pending.aggregate(
            Sum('total_value'))['total_value__sum'] or 0

    payments_pending = payments.models.Payment.sales_pending()
    payments_pending_total = payments_pending.aggregate(
            Sum('total_value'))['total_value__sum'] or 0



    invoices_pending_by_customer = invoices_pending.values(
            'customer__name', 'customer').annotate(
                    count=Count('customer')).order_by('-count')

    payments_pending_by_customer = payments_pending.values(
            'customer__name', 'customer').annotate(
                    count=Count('customer')).order_by('-count')

    # dict to render in template
    dashboard = {
        'customer': customers.models.Customer.objects.all(),
        'invoices_pending': invoices_pending,
        'invoices_pending_total': invoices_pending_total,
        'invoices_pending_by_customer': invoices_pending_by_customer,
        'payments_pending': payments_pending,
        'payments_pending_total': payments_pending_total,
        'payments_pending_by_customer': payments_pending_by_customer,
        'table_pending': sales.tables.SaleTable,

    }
    return render(request, 'home.html', {'dashboard': dashboard})
