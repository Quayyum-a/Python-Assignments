import unittest
import anagramfunction

class TestAnagramWords(unittest.TestCase):
    def test_that_anagram_function_returns_true(self):
        actual = anagramfunction.get_anagram("listen", "silent")
        result = True
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()