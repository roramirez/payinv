from django.conf.urls import include, url
from . import views

urlpatterns = [
    # sale
    url(r'^add/$', views.SaleEditView.as_view(),
        name='sale_add'),
    url(r'^$', views.SaleListView.as_view(), name='sale_list'),
    url(r'^$', views.SaleListView.as_view(), name='index'),  # homeme
    url(r'^(?P<pk>[\w-]+)/$', views.sale, name='sale'),
    url(r'^(?P<pk>[\w-]+)/edit/$',
        views.SaleEditView.as_view(),
        name='sale_edit'),


]
