from django.test import TestCase
from app.calc import add,subtract

class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test two numbers are added together"""
        self.assertEqual(add(3,8),11)
    
    def test_subtract_numbers(self):
        """Test Values are subtracted and returned"""
        self.assertEqual(subtract(5,11),6)