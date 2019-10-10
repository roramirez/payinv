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

    def test_search_not_found(self):
        """ Should not returns esults """
        client = Client()
        SaleFactory(internal_id="ABC-123")
        SaleFactory(internal_id="ABC")
        response = client.get('/sales/?q=ABCd:w')
        self.assertEqual(len(response.context['table'].data), 0)

    def test_search_found(self):
        """ Should returns two results """
        client = Client()
        SaleFactory(internal_id="123")
        SaleFactory(internal_id="ABC-123")
        SaleFactory(internal_id="ABC")
        response = client.get('/sales/?q=ABC')
        self.assertEqual(len(response.context['table'].data), 2)

    def test_search_found_and_redirect(self):
        """ Should return one result and redirect """
        client = Client()
        SaleFactory(internal_id="123")
        SaleFactory(internal_id="ABC-123")
        response = client.get('/sales/?q=ABC-123')
        self.assertEqual(response.status_code, 302)
        self.assertIsNone(response.context)
