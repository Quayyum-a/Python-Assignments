import unittest
import factorialfunction

class TestFactorialNumber(unittest.TestCase):
    def test_that_factorial_function_returns_correct(self):
        actual = factorialfunction.get_factorial(5)
        result = 120
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()