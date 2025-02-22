import unittest
import primefunction

class TestNumberIsPrime(unittest.TestCase):
    def test_that_anagram_function_returns_true(self):
        actual = primefunction.get_prime(9)
        result = True
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()