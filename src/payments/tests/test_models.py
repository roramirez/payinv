from django.test import TestCase
from core.tests.factories import SaleFactory, PaymentFactory
from payments.models import Payment


class PaymentModelTestCase(TestCase):

    def test_sales_pending_without_payment(self):
        """ Should return this sale if not have Payment to cover"""
        sale = SaleFactory(total_value=100)
        self.assertCountEqual(Payment.sales_pending().all(), [sale])

    def test_sales_pending_with_payment_not_all_value(self):
        """ Should return this sale if has payments for not all total_value"""
        sale = SaleFactory(total_value=1000)
        PaymentFactory(sale=sale, total_value=50)
        PaymentFactory(sale=sale, total_value=50)
        self.assertCountEqual(Payment.sales_pending().all(), [sale])

    def test_sales_pending_with_payment_for_all_value(self):
        """ Should return not sale if has payments for all total_value"""
        sale = SaleFactory(total_value=1000)
        PaymentFactory(sale=sale, total_value=500)
        PaymentFactory(sale=sale, total_value=500)
        self.assertEqual(Payment.sales_pending().count(), 0)

    def test_sales_pending_with_payment_for_most_all_value(self):
        """ Should return not sale if has payments for all total_value"""
        sale = SaleFactory(total_value=1000)
        PaymentFactory(sale=sale, total_value=1500)
        PaymentFactory(sale=sale, total_value=500)
        self.assertEqual(Payment.sales_pending().count(), 0)
