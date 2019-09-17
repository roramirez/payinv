from django.conf.urls import include, url
from . import views

urlpatterns = [
    # customer
    url(r'^add/$', views.CustomerEditView.as_view(),
        name='customer_add'),
    url(r'^$', views.CustomerListView.as_view(), name='customer_list'),
    url(r'^$', views.CustomerListView.as_view(), name='index'),  # homeme
    url(r'^(?P<pk>[\w-]+)/$', views.customer, name='customer'),
    url(r'^(?P<pk>[\w-]+)/edit/$',
        views.CustomerEditView.as_view(),
        name='customer_edit'),


]
