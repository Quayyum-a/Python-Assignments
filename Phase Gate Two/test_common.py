import unittest
import commonfunction

class TestCommonNumber(unittest.TestCase):
    def test_that_common_number_is_found(self):
        actual = commonfunction.get_common([1,2,3], [3,4,5])
        result = [3]
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()