import unittest
import capitalisefunction

class TestCapitaliseWords(unittest.TestCase):
    def test_that_anagram_function_returns_correct(self):
        actual = capitalisefunction.get_capital(["apple", "banana", "cherry"])
        result = ["Apple", "Banana", "Cherry"]
        self.assertEqual(actual, result)
        
        
        
if __name__ =="__main__":
    unittest.main()