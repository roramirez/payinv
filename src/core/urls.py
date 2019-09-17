from django.conf.urls import include, url
from . import views
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create', views.create, name='create'),

    url(r'^register/$',
        RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'),

    url(r'', include('registration.backends.hmac.urls')),
    # company
    url(r'^company/add/$', views.CompanyEditView.as_view(),
        name='company_add'),
    url(r'^company/$', views.CompanyListView.as_view(), name='company_list'),
    url(r'^company/(?P<pk>[\w-]+)/$', views.company, name='company'),
    url(r'^company/(?P<pk>[\w-]+)/edit/$',
        views.CompanyEditView.as_view(),
        name='company_edit'),

    # api_key
    url(r'^api_key/add/$', views.ApiKeyEditView.as_view(), name='api_key_add'),
    url(r'^api_key/$', views.ApiKeyListView.as_view(), name='api_key_list'),
    url(r'^api_key/(?P<pk>[\w-]+)/$', views.api_key, name='api_key'),
    url(r'^api_key/(?P<pk>[\w-]+)/edit/$',
        views.ApiKeyEditView.as_view(),
        name='api_key_edit'),

    # process file
    url(r'^process_file/$', views.ProcessFileListView.as_view(),
        name='process_file_list'),
    url(r'^process_file/(?P<uuid>[\w-]+)/$', views.get_process_file,
        name='process_file'),

]
