import unittest
import todolistmanager

class TestToDoListManager(unittest.TestCase):
    def test_that_to_do_list_prints_menu(self):
        actual = todolistmanager.get_menu()
        expected = """\n1. Add a task
2. View tasks
3. Mark task as complete
4. Delete a task
5. Exit"""
        self.assertEqual(actual, expected)
        
    def test_that_to_do_list_prints_choice(self):
        actual = todolistmanager.get_choice()
        self.assertIsInstance(actual, int)
        
    def test_that_to_do_list_add_task(self):
        actual = todolistmanager.add_task()
        result = "Buy groceries"
        self.assertEqual(actual, result)
        
    def test_that_to_do_list_view_task(self):
        todolistmanager.tasks = []  
        actual = todolistmanager.view_tasks()
        self.assertEqual(actual, "No task recorded yet.")  
        
        todolistmanager.tasks.append({"task": "Buy groceries"})  
        actual = todolistmanager.view_tasks()
        expected = "Tasks:\n1 [] Buy groceries" 
        self.assertEqual(actual, expected)
        
    def test_that_to_do_list_mark_complete(self):
        tasks = [{"task": "Buy groceries", "completed": False}]
        task_number = 0  
        tasks[task_number]["completed"] = True 

        expected = True
        actual = tasks[task_number]["completed"]
        
        self.assertTrue(actual, expected)
        
    def test_that_to_do_list_delete_task(self):
        todolistmanager.tasks = [{"task": "Buy groceries"}, {"task": "Make Money"}]
        actual = todolistmanager.tasks.pop(0)  
        result = {"task": "Buy groceries"}  
        self.assertEqual(actual, result)

    def test_that_to_do_list_exits_(self):
        actual = todolistmanager.exit_app()
        self.assertEqual(actual, "\nExiting the app. Goodbye!")



    
if __name__ == "__main__":
    unittest.main()
