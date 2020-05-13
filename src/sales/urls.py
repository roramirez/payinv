from django.conf.urls import url
from . import views

urlpatterns = [
    # sale
    url(r'^add/$', views.SaleEditView.as_view(),
        name='sale_add'),
    url(r'^$', views.SaleListView.as_view(), name='sale_list'),
    url(r'^pending/invoice/$', views.SaleListPendingInvoice.as_view(),
        name='sale_list_pending_invoice'),
    url(r'^pending/payment/$', views.SaleListPendingPayment.as_view(),
        name='sale_list_pending_payment'),

    url(r'^new/customer/(?P<customer_id>[\w-]+)/$',
        views.SaleAddToCustomer.as_view(),
        name='sale_to_customer'),
    url(r'^(?P<pk>[\w-]+)/$', views.sale, name='sale'),
    url(r'^(?P<pk>[\w-]+)/edit/$',
        views.SaleEditView.as_view(),
        name='sale_edit'),

]
