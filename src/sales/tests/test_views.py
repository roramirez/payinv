from django.test import TestCase
from django.test import Client
from core.tests.factories import SaleFactory
from django.urls import reverse_lazy


class SalesViewTestCase(TestCase):

    def test_export(self):
        SaleFactory(total_value=1000)
        client = Client()

        response = client.get('/sales/?export')
        self.assertEqual(response['Content-Type'], 'text/csv')
        self.assertEqual(response.status_code, 200)

    def test_pending_invoice_table(self):
        """ should return invoice table"""
        SaleFactory(total_value=193456, notes="This note is for sale")

        client = Client()
        url = reverse_lazy('sale_list_pending_invoice')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '193456')
