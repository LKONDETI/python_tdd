from src.katas import fizz_buzz
import unittest


class FizzBuzz_test(unittest.TestCase):

   
   
    def test_it_return_fizz_for_three(self):
        converter = fizz_buzz.FizzBuzz()

        for number in [3]:
            self.assertEqual('Fizz', converter.convert(number))

    def test_it_return_fizz_for_four(self):
        converter = fizz_buzz.FizzBuzz()
        for number in [4]:
            self.assertEqual(number, converter.convert(number))

    def test_it_return_fizz_for_five(self):
        converter = fizz_buzz.FizzBuzz()

        for number in [5]:
            self.assertEqual('Buzz', converter.convert(number))
    
    def test_it_return_buzz_for_multiples_of_five(self):
       converter = fizz_buzz.FizzBuzz()

       for number in [5, 10, 20, 25]:
          self.assertEqual('Buzz', converter.convert(number))

    def test_it_return_fizzbuzz_for_multiples_of_three_and_five(self):
        converter = fizz_buzz.FizzBuzz()

        for number in [15, 30, 45, 60]:
            self.assertEqual('FizzBuzz', converter.convert(number))

    def test_it_return_the_original_number_if_not_divisible_by_three_and_five(self):
        converter = fizz_buzz.FizzBuzz()
        for number in [1, 2, 4, 7]:
           self.assertEqual(number, converter.convert(number))
