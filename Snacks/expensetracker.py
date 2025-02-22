def get_heading():
    return "Welcome to Semicolon Expense Tracker App"

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
                date = input("Enter the date (YYYY-MM-DD): ")
                description = input("Enter the description: ")

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


