"""
Test sample
"""
from django.test import SimpleTestCase

from rest_framework.test import APIClient
# from app import calc


# class CalcTests(SimpleTestCase):
#     def test_add_numbers(self):
#         result = calc.add(5, 6)
#         self.assertEqual(result, 11)
#
#     def test_subtract_numbers(self):
#         result = calc.subtract(15, 10)
#         self.assertEqual(result, 5)

class TestViews(SimpleTestCase):
    def test_get_greeting(self):
        client = APIClient()
        result = client.get('/greetings/')

        self.assertEqual(result.status_code, 200)
        # self.assertEqual(result.data, ['Hello', 'Bonjour', 'Hola'])