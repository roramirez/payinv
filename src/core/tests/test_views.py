from django.test import TestCase
from django.test import Client


class CoreViewTestCase(TestCase):

    def test_homepage(self):
        client = Client()

        response = client.get('/')
        self.assertEqual(response.status_code, 200)
