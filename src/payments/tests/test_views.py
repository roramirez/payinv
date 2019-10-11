from django.test import TestCase
from django.test import Client
from core.tests.factories import SaleFactory, PaymentFactory
from django.urls import reverse_lazy


class PaymentViewTestCase(TestCase):

    def test_not_found_sale_for_add_payment(self):
        """
        Should return a 404 not found for add new payment a not exists sale
        """
        client = Client()
        url = reverse_lazy('payment_to_sale', kwargs={'sale_id': 1000})
        response = client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_add_sale_for_add_payment(self):
        """ should return a 200 OK for add new payment to sale"""
        sale = SaleFactory()
        client = Client()
        url = reverse_lazy('payment_to_sale', kwargs={'sale_id': sale.id})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['sale'], sale)
        self.assertEqual(response.context['obj'], None)

    def test_search_found_payments(self):
        """ Should returns two results """
        client = Client()
        PaymentFactory(total_value=1500)
        PaymentFactory(total_value=1501)
        response = client.get('/payments/?q=150')
        self.assertEqual(len(response.context['table'].data), 2)

    def test_search_not_found_payments(self):
        """ Should not returns results """
        client = Client()
        PaymentFactory(total_value=1501)
        response = client.get('/payments/?q=ABC')
        self.assertEqual(len(response.context['table'].data), 0)
