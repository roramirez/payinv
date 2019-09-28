from django.conf.urls import url
from . import views

urlpatterns = [
    # payment
    url(r'^add/$', views.PaymentEditView.as_view(),
        name='payment_add'),
    url(r'^$', views.PaymentListView.as_view(), name='payment_list'),
    url(r'^(?P<pk>[\w-]+)/$', views.payment, name='payment'),
    url(r'^new/sale/(?P<sale_id>[\w-]+)/$', views.PaymentAddToSale.as_view(),
        name='payment_to_sale'),
    url(r'^(?P<pk>[\w-]+)/edit/$',
        views.PaymentEditView.as_view(),
        name='payment_edit'),
]
