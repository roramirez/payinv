from django.test import TestCase
from django.test import Client
from core.tests.factories import SaleFactory, InvoiceFactory
from django.urls import reverse_lazy


class InvoiceViewTestCase(TestCase):

    def test_not_found_sale_for_add_invoice(self):
        """
        Should return a 404 not found for add new invoice a not exists sale
        """
        client = Client()
        url = reverse_lazy('invoice_to_sale', kwargs={'sale_id': 1000})
        response = client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_add_sale_for_add_invoice(self):
        """ should return a 200 OK for add new invoice to sale"""
        sale = SaleFactory()
        client = Client()
        url = reverse_lazy('invoice_to_sale', kwargs={'sale_id': sale.id})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['sale'], sale)
        self.assertEqual(response.context['obj'], None)

    def test_search_found_payments(self):
        """ Should returns two results """
        client = Client()
        InvoiceFactory(internal_id=1500)
        InvoiceFactory(internal_id=1501)
        response = client.get('/invoices/?q=150')
        self.assertEqual(len(response.context['table'].data), 2)

    def test_search_not_found_payments(self):
        """ Should not returns results """
        client = Client()
        InvoiceFactory(internal_id=1501)
        response = client.get('/invoices/?q=ABC')
        self.assertEqual(len(response.context['table'].data), 0)

    def test_not_found_invoice_edit(self):
        """
        Should return a 404 not found for not PK for Invoice
        """
        client = Client()
        url = reverse_lazy('invoice_edit', kwargs={'pk': 9669})
        response = client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_not_found_invoice(self):
        """
        Should return a 404 not found for not PK for Invoice EDIT
        """
        client = Client()
        url = reverse_lazy('invoice', kwargs={'pk': 9669})
        response = client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_not_found_invoice_200(self):
        """
        Should return a 200  found PK
        """

        invoice = InvoiceFactory(total_value=1500)
        client = Client()
        url = reverse_lazy('invoice', kwargs={'pk': invoice.id})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
