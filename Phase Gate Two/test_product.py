import unittest
import productfunction

class TestProductAndSum(unittest.TestCase):
    def test_that_product_function_returns_correct(self):
        actual = productfunction.get_product_and_sum([1,2,3,5,6])
        result = [30]
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()