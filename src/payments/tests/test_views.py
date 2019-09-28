from django.test import TestCase
from django.test import Client
from core.tests.factories import SaleFactory
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
