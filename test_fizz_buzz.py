from unittest import TestCase
from fizz_buzz import FizzBuzz

class FizzBuzzTest(TestCase):

    def setUp(self):
        self.fizz_buzz = FizzBuzz()

    def test_fizz_buzz(self):
        result = self.fizz_buzz.fizz_buzz(15)
        self.assertEqual(result, 'FizzBuzz')



    
