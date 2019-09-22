from django.conf.urls import include, url
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView

urlpatterns = [

    url(r'^register/$',
        RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'),

    url(r'', include('registration.backends.hmac.urls')),

]
