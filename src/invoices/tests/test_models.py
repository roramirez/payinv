from django.test import TestCase
from core.tests.factories import SaleFactory, InvoiceFactory
from invoices.models import Invoice


class InvoiceModelTestCase(TestCase):

    def test_sales_pending_without_invoice(self):
        """ Should return this sale if not have Invoice to cover"""
        sale = SaleFactory(total_value=100)
        self.assertCountEqual(Invoice.sales_pending().all(), [sale])

    def test_sales_pending_with_invoice_not_all_value(self):
        """ Should return this sale if has invoices for not all total_value"""
        sale = SaleFactory(total_value=1000)
        InvoiceFactory(sale=sale, total_value=50)
        InvoiceFactory(sale=sale, total_value=50)
        self.assertCountEqual(Invoice.sales_pending().all(), [sale])

    def test_sales_pending_with_invoice_for_all_value(self):
        """ Should return not sale if has invoices for all total_value"""
        sale = SaleFactory(total_value=1000)
        InvoiceFactory(sale=sale, total_value=500)
        InvoiceFactory(sale=sale, total_value=500)
        self.assertEqual(Invoice.sales_pending().count(), 0)

    def test_sales_pending_with_invoice_for_most_all_value(self):
        """ Should return not sale if has invoices for all total_value"""
        sale = SaleFactory(total_value=1000)
        InvoiceFactory(sale=sale, total_value=1500)
        InvoiceFactory(sale=sale, total_value=500)
        self.assertEqual(Invoice.sales_pending().count(), 0)
