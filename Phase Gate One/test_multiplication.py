import unittest
import multiplicationfunction

class TestMultiplicationFunction(unittest.TestCase):
    def test_that_multiplication_function_exists(self):
        multiplicationfunction.get_multiplication(3, 2)
        
    def test_that_multiplication_function_return_correct_value(self):
        actual = multiplicationfunction.get_multiplication(3, 2)
        result = 6 
        self.assertEqual(actual, result)
        
    def test_that_multiplication_function_return_zero(self):
        actual = multiplicationfunction.get_multiplication(0, 3)
        result = 0
        self.assertEqual(actual, result)
        
    def test_that_multiplication_function_return_with_decimal_value(self):
        actual = multiplicationfunction.get_multiplication(5.3, 3)
        result = 15.9
        self.assertEqual(actual, result)    
        
    def test_that_multiplication_function_return_invalid_input(self):
        actual = multiplicationfunction.get_invalid('a', 3)
        result = 'invalid input'
        self.assertEqual(actual, result)