expense = []
def get_heading():
    return "Welcome to Semicolon Expense Tracker App"

def get_menu():
    return """\n1. Add an expense
2. View all expenses
3. Calculate total expenses
4. Exit"""

def get_choice():
    choice = input("Enter your choice: ")
    if not choice.isdigit() or int(choice) not in range(1, 5):
        raise ValueError("Invalid choice. Please enter a number between 1 and 4.")
    return int(choice)

def get_date():
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")

        if len(date) == 10 and date[4] == "-" and date[7] == "-":
            parts = date.split("-")
            if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                return date
        print("Invalid format. Try again using YYYY-MM-DD.")

def get_description():
    while True:
        description = input("Enter the description: ").strip()
        if description.replace(" ", "").isalpha():  
            return description
        else:
            print("Invalid input! Please enter only letters A-Z.")

def get_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                return amount
        except ValueError:
            print("Invalid amount. Enter a valid number.")   
            
            
def view_expenses():
    if not expenses:
        return "No expenses recorded yet."
    else:
        result = "Expenses:\n"
        for expense in expenses:
            result += f"Date: {expense['date']}, Description: {expense['description']}, Amount: ₦{expense['amount']:.2f}\n"
        return result.strip()

def calculate_expenses():
    if not expenses:
        return "\nTotal Expenses: ₦0.00"
    else:
        total = sum(expense['amount'] for expense in expenses)
        return f"\nTotal Expenses: ₦{total:.2f}"

def exit_app():
    return "\nExiting the app. Goodbye!"
    




def create_menu():
    expenses = []  
    
    print(get_heading())

    while True:
        print("\n1. Add an expense")
        print("2. View all expenses")
        print("3. Calculate total expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            continue

        choice = int(choice)

        match choice:
            case 1:
                while True:
                    date = input("Enter the date (YYYY-MM-DD): ")

                    if len(date) == 10 and date[4] == "-" and date[7] == "-":
                        parts = date.split("-")

                        if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
                            break

                    print("Try again. Use YYYY-MM-DD format.")

                while True:
                    description = input("Enter the description: ")
    
                    if description.replace(" ", "").isalpha():  
                        break  
                    else:
                        print("Invalid input! Please enter only letters A-Z")

                try:
                    amount = float(input("Enter the amount: "))
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                        continue
                except ValueError:
                    print("Invalid amount. Enter a valid number.")
                    continue

                expenses.append({"date": date, "description": description, "amount": amount})
                print("\nExpense added!")

            case 2:
                if not expenses:
                    print("\nNo expenses recorded yet.")
                else:
                    print("\n Expenses: ")
                    for expense in expenses:
                        print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: ₦{expense['amount']:.2f}")

            case 3:
                if not expenses:
                    print("\nTotal Expenses: ₦0.00")
                else:
                    total = sum(expense['amount'] for expense in expenses)
                    print(f"\nTotal Expenses: ₦{total:.2f}")

            case 4:
                print("\nExiting the app. Goodbye!")
                break

            case _:
                print("\nInvalid choice. Try again.")

if __name__=="__main__":
    create_menu()

