from django.test import TestCase
from django.test import Client
from core.tests.factories import SaleFactory


class SalesViewTestCase(TestCase):

    def test_export(self):
        SaleFactory(total_value=1000)
        client = Client()

        response = client.get('/sales/?export')
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertEqual(response.status_code, 200)
