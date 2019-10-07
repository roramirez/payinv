from django.test import TestCase
from core.tests.factories import SaleFactory, PaymentFactory, InvoiceFactory


class SaleModelTestCase(TestCase):

    def test_total_payments_in_cero(self):
        """ Should return cero for sales without payments"""
        sale = SaleFactory(total_value=100)
        self.assertEqual(sale.total_payments, 0)

    def test_total_invoices_in_cero(self):
        """ Should return cero for sales without invoices"""
        sale = SaleFactory(total_value=100)
        self.assertEqual(sale.total_invoices, 0)

    def test_total_payments(self):
        """ Should return total value for payments of sale"""
        sale = SaleFactory(total_value=1000)
        PaymentFactory(sale=sale, total_value=50)
        PaymentFactory(sale=sale, total_value=50)
        self.assertEqual(sale.total_payments, 100)

    def test_total_invoices(self):
        """ Should return total value for invoices of sale"""
        sale = SaleFactory(total_value=1000)
        InvoiceFactory(sale=sale, total_value=50)
        InvoiceFactory(sale=sale, total_value=500)
        self.assertEqual(sale.total_invoices, 550)

    def test_to_csv(self):
        """ Should return value sale in export sales"""
        sale = SaleFactory(total_value=12347)
        self.assertIn('12347',  sale.to_csv())
