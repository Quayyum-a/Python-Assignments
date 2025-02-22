import unittest
import vowelsfunction

class TestHowManyVowelsInAWord(unittest.TestCase):
    def test_function_returns_correct(self):
        actual = vowelsfunction.get_vowels("python is sweet")
        result = 4
        self.assertEqual(actual, result)
        
    def test_function_returns_correct_again(self):
        actual = vowelsfunction.get_vowels("java is sweeter")
        result = 6
        self.assertEqual(actual, result)
        
        
        
        
if __name__ == "__main__":
    unittest.main()