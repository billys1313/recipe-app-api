"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """test the calc mode."""

    def test_add_numbers(self):
        """test add numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        """test sub numbers together"""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)