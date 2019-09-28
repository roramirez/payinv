from django.conf.urls import url
from . import views

urlpatterns = [
    # invoice
    url(r'^add/$', views.InvoiceEditView.as_view(),
        name='invoice_add'),
    url(r'^$', views.InvoiceListView.as_view(), name='invoice_list'),
    url(r'^(?P<pk>[\w-]+)/$', views.invoice, name='invoice'),
    url(r'^new/sale/(?P<sale_id>[\w-]+)/$', views.InvoiceAddToSale.as_view(),
        name='invoice_to_sale'),
    url(r'^(?P<pk>[\w-]+)/edit/$',
        views.InvoiceEditView.as_view(),
        name='invoice_edit'),
]
