from django.conf.urls import include, url
from . import views

urlpatterns = [
    # invoice
    url(r'^add/$', views.InvoiceEditView.as_view(),
        name='invoice_add'),
    url(r'^$', views.InvoiceListView.as_view(), name='invoice_list'),
    url(r'^$', views.InvoiceListView.as_view(), name='index'),  # homeme
    url(r'^(?P<pk>[\w-]+)/$', views.invoice, name='invoice'),
    url(r'^(?P<pk>[\w-]+)/edit/$',
        views.InvoiceEditView.as_view(),
        name='invoice_edit'),


]
