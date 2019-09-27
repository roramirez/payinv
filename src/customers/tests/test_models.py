from django.test import TestCase
from core.tests.factories import (
    SaleFactory, CustomerFactory, PaymentFactory, InvoiceFactory)


class SaleModelTestCase(TestCase):

    def test_total_sales_in_cero(self):
        """ Should return cero for sales for customer"""
        customer = CustomerFactory()
        self.assertEqual(customer.total_sales, 0)

    def test_total_sales(self):
        """ Should return total_values for sales for customer"""
        customer = CustomerFactory()
        SaleFactory(customer=customer, total_value=1)
        SaleFactory(customer=customer, total_value=11)
        self.assertEqual(customer.total_sales, 12)

    def test_total_payments(self):
        """ Should return total_values for payments for customer"""
        customer = CustomerFactory()
        sale = SaleFactory(customer=customer)
        PaymentFactory(sale=sale, total_value=100)
        PaymentFactory(sale=sale, total_value=101)
        self.assertEqual(customer.total_payments, 201)

    def test_total_invoices(self):
        """ Should return total_values for invoices customer"""
        customer = CustomerFactory()
        sale = SaleFactory(customer=customer)
        InvoiceFactory(sale=sale, total_value=102)
        InvoiceFactory(sale=sale, total_value=103)
        self.assertEqual(customer.total_invoices, 205)
