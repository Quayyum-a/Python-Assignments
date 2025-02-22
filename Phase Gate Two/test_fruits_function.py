import unittest
import fruitsfunction

class TestFruitsFunction(unittest.TestCase):
    def test_that_fruit_function_returns_correct(self):
        actual = fruitsfunction.get_fruits(["mango","grape","apple","banana"])
        result = ['MANGO', 'GRAPE', 'APPLE', 'BANANA']
        self.assertEqual(actual, result)
        
        
    def test_that_fruit_function_returns_square(self):
        actual = fruitsfunction.get_square([2,5,3,4,2])
        result = 65
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()