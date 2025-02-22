import unittest
import mergefunction

class TestMergeList(unittest.TestCase):
    def test_that_merge_function_returns_correct(self):
        actual = mergefunction.merge_list([1,3,4], [5,6,7])
        result = [1,5,3,6,4,7]
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()