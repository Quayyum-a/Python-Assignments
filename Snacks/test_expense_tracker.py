import unittest
import expensetracker

class TestExpenseTracker(unittest.TestCase):  
    def test_that_expense_tracker_prints_heading(self):
        actual = expensetracker.get_heading()
        self.assertEqual(actual, "Welcome to Semicolon Expense Tracker App")
    
    def test_that_expense_tracker_prints_menu(self):
        actual = expensetracker.get_menu()
        expected = """\n1. Add an expense
2. View all expenses
3. Calculate total expenses
4. Exit"""
        self.assertEqual(actual, expected)

    def test_that_expense_tracker_prints_choice(self):
        actual = expensetracker.get_choice()
        self.assertIsInstance(actual, int)
        
    def test_that_expense_tracker_prints_date(self):
        actual = expensetracker.get_date()
        result = "2025-12-17"
        self.assertEqual(actual, result)
        
    def test_that_expense_tracker_prints_description(self):
        actual = expensetracker.get_description()
        result = "groceries"
        self.assertEqual(actual, result)
        
    def test_that_expense_tracker_prints_amount(self):
        actual = expensetracker.get_amount()
        self.assertGreater(actual, 0)

    def test_that_expense_tracker_views_expenses(self):
        expensetracker.expenses = []  
        actual = expensetracker.view_expenses()
        self.assertEqual(actual, "No expenses recorded yet.")  
        
        expensetracker.expenses.append({"date": "2025-12-17", "description": "Lunch", "amount": 1500.00})
        actual = expensetracker.view_expenses()
        expected = "Expenses:\nDate: 2025-12-17, Description: Lunch, Amount: ₦1500.00"  
        self.assertEqual(actual, expected)


    def test_that_expense_tracker_calculates_expenses(self):
        expensetracker.expenses = [] 
        actual = expensetracker.calculate_expenses()
        self.assertEqual(actual, "\nTotal Expenses: ₦0.00")

        expensetracker.expenses.append({"date": "2025-12-17", "description": "Lunch", "amount": 1500.00})
        expensetracker.expenses.append({"date": "2025-12-18", "description": "Transport", "amount": 500.00})
        actual = expensetracker.calculate_expenses()
        self.assertEqual(actual, "\nTotal Expenses: ₦2000.00")

    def test_that_expense_tracker_exits_app(self):
        actual = expensetracker.exit_app()
        self.assertEqual(actual, "\nExiting the app. Goodbye!")

if __name__ == "__main__":
    unittest.main()
