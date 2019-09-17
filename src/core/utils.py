from django.utils.translation import ugettext as _


def yes_or_no(value):
    return _('Yes') if value else _('No')
