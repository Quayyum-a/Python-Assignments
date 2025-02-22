import unittest
import duplicatefunction

class TestDuplicateNumbers(unittest.TestCase):
    def test_that_duplicate_function_returns_correct(self):
        actual = duplicatefunction.get_duplicate([1,2,3,5,6,2])
        result = True
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()