import unittest
import functionfortaskfour

class TestSumOfAllDigits (unittest.TestCase):
    
    def test_that_the_last_digit_is_gotten(self):
        actual = functionfortaskfour.get_digit(89)
        result = 9
        self.assertEqual(actual, result)
    
    def test_that_the_last_digit_is_truncuated(self):
        actual = functionfortaskfour.remove_digit(89)
        result = 8
        self.assertEqual(actual, result)
        
    def test_that_function_return_negative_value_with_negative_parameter(self):
        actual = functionfortaskfour.get_digit(-6)
        result = 'invalid data'
        self.assertEqual(actual, result)  
        
    def test_that_function_return_correct_value_with_decimal_input(self):
        actual = functionfortaskfour.get_digit(3.25)
        result = 3.25
        self.assertEqual(actual, result)
          
    def test_that_function_return_invalid_input(self):
        actual = functionfortaskfour.get_digit('a')
        result = 'invalid data'
        self.assertEqual(actual, result)