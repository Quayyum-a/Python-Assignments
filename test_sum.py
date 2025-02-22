import unittest
import sumfunction

class TestEvenNumberSum(unittest.TestCase):
    def test_that_sum_function_exists(self):
        actual = sumfunction.sum_even_numbers([2, 7, 5, 11, 7, 19, 2, 8, 0])
        result = 12
        self.assertEqual(actual, result)
        
        
        
if __name__ == "__main__":
    unittest.main()
