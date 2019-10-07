# -*- coding: utf-8 -*-
"""Factory of all models."""
import factory
import factory.fuzzy
from customers.models import Customer
from sales.models import Sale
from invoices.models import Invoice
from payments.models import Payment
import datetime


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker('company')
    active = True
    cid = factory.Faker('ssn')
    address = factory.Faker('address')


class SaleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sale

    customer = factory.SubFactory(CustomerFactory)
    internal_id = factory.Sequence(lambda n: 'ID-%s' % n)
    total_value = factory.fuzzy.FuzzyInteger(10000, 100000)
    concept = factory.Sequence(lambda n: 'Concept-%s' % n)
    notes = factory.Faker("paragraphs", nb=1, ext_word_list=None)
    done_at = factory.fuzzy.FuzzyDate(datetime.date(2017, 11, 1))


class InvoiceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Invoice

    sale = factory.SubFactory(SaleFactory)
    internal_id = factory.Sequence(lambda n: 'ID-%s' % n)
    total_value = factory.fuzzy.FuzzyInteger(10000, 100000)
    notes = factory.Faker("paragraphs", nb=3, ext_word_list=None)
    date_to_pay = factory.fuzzy.FuzzyDate(datetime.date(2017, 11, 1))
    date_issue = factory.fuzzy.FuzzyDate(datetime.date(2017, 11, 1))


class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Payment

    sale = factory.SubFactory(SaleFactory)
    total_value = factory.fuzzy.FuzzyInteger(10000, 100000)
    notes = factory.Faker("paragraphs", nb=3, ext_word_list=None)
    pay_at = factory.fuzzy.FuzzyDate(datetime.date(2017, 11, 1))
