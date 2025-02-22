import unittest
import expensetracker

class TestExpenseTracker(unittest.TestCase):
    def test_that_expense_tracker_prints_header(self):
        actual = expensetracker.get_heading()
        result = "Welcome to Semicolon Expense Tracker App"
        self.assertEqual(actual,result)
        
    def test_that_expense_tracker_prints_menu(self):
        actual = expensetracker.create_menu()
        
        
        
        
        
        
if __name__ =="__main__":
    unittest.main()