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
    while True:
        choice = input("Enter your choice: ")
        if choice.isdigit() and int(choice) in range(1, 6):
            return int(choice)
        print("Invalid choice. Please enter a number between 1 and 5.")
    
def add_task():
    while True:
        task = input("Enter a task: ").strip()
        if task.replace(" ", "").isalpha():  
            tasks.append({"task": task, "completed": False})  
            print("Task added successfully!")
            break
        print("Invalid input! Please enter only letters A-Z.")
        
def view_tasks():
    if not tasks:
        print("No tasks recorded yet.")
    else:
        print("Tasks:")
        for count, task in enumerate(tasks, start=1):  
            status = "[x]" if task.get("completed") else "[]"  
            print(f"{count}. {status} {task['task']}")
        

def mark_complete():
    if not tasks:
        print("No tasks to mark as complete.")
        return
    
    while True:
        try:
            task_number = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]["completed"] = True  
                print(f"Task '{tasks[task_number]['task']}' marked as complete.")
                break
            else:
                print("Invalid task number. Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")
        

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return
    
    while True:
        try:
            task_number = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_number < len(tasks):
                deleted_task = tasks.pop(task_number)
                print(f"Task '{deleted_task['task']}' deleted successfully.")
                break
            else:
                print("Invalid task number. Please enter a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def exit_app():
    print("\nExiting the app. Goodbye!")
    

def get_main():
    print(get_heading())
    
    while True:
        print(get_menu())
        choice = get_choice()
        
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_complete()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            exit_app()
            break

if __name__ == "__main__":
    get_main()
