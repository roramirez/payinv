from django.test import TestCase
from core.utils import yes_or_no
from django.utils.translation import ugettext as _


class UtilsTestCase(TestCase):

    def test_yes_or_no(self):
        self.assertEqual(yes_or_no(True), _('Yes'))
        self.assertEqual(yes_or_no(False), _('No'))
        self.assertEqual(yes_or_no(None), _('No'))
