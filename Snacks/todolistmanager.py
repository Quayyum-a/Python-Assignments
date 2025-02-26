tasks = []  

def get_heading():
    return "To-Do List Manager"
    
def get_menu():
    return """\n1. Add a task
2. View tasks
3. Mark task as complete
4. Delete a task
5. Exit"""

def get_choice():
    choice = input("Enter your choice: ")
    if not choice.isdigit() or int(choice) not in range(1, 6):
        raise ValueError("Invalid choice. Please enter a number between 1 and 5.")
    return int(choice)
    
def add_task():
    while True:
        task = input("Enter a task: ").strip()
        if task.replace(" ", "").isalpha():  
            tasks.append({"task": task})  
            return task
        else:
            print("Invalid input! Please enter only letters A-Z.")
        
def view_tasks():
    if not tasks:
        return "No task recorded yet."
    else:
        result = "Tasks:\n"
        for count, task in enumerate(tasks, start = 1):  
            status = "[x]" if task.get("completed") else "[]"  
            result += f"{count} {status} {task['task']}\n"  
        return result.strip()
        
        
def mark_complete():
    if not tasks:
        print("No tasks to mark as complete.")
        return
    task_number = int(input("Enter the task number to mark as complete: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True  
        print(f"Task '{tasks[task_number]['task']}' completed.")
    else:
        print("Invalid task number. Please enter a valid number.")
        
        
def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            deleted_task = tasks.pop(task_number)
            print(f"Task '{deleted_task['task']}' deleted successfully.")
        else:
            print("Invalid task number. Please enter a valid number.")
    except ValueError:
        print("Invalid input! Please enter a number.")


def exit_app():
    return "\nExiting the app. Goodbye!"
    
    
def get_main():
    tasks = []
    
    print(get_heading())
    
    while True:
        print("\n1. Add a task")
        print("2. View all expenses")
        print("3. Calculate total expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
if__name__=="__main__":
        get_menu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       