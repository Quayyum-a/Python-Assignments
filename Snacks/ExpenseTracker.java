import java
import java.util.Scanner;

public class ExpenseTracker {
    public String getHeader() {
        return "Welcome to Semicolon Expense Tracker App";
    }
    
    public static String getMenu(){
       return  "\n1. Add an expense\n2. View all expenses\n3. Calculate total expenses\n4. Exit";
    }
    
    public static int getChoice() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your choice: ");
        String choice = scanner.nextLine();

        if (!choice.matches("[1-4]")) {
            throw new IllegalArgumentException("Invalid choice. Please enter a number between 1 and 4.");
        }

        return Integer.parseInt(choice);
    }
    
    
    public static String getDate(){
       Scanner scanner = new Scanner (System.in);
       while (true) {
            System.out.print("Enter the date (YYYY-MM-DD): ");
            String date = scanner.nextLine();

            if (date.matches("\\d{4}-\\d{2}-\\d{2}")) {
                return date;
            }

            System.out.println("Invalid format. Try again using YYYY-MM-DD.");
        }
    }
    
     
    public static String getDescription() {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Enter the description: ");
            String description = scanner.nextLine().trim();

            if (description.replace(" ", "").matches("[a-zA-Z]+")) {
                return description;
            } else {
                System.out.println("Invalid input! Please enter only letters A-Z.");
            }
        }
    }
    
    public static double getAmount() {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            try {
                System.out.print("Enter the amount: ");
                double amount = Double.parseDouble(scanner.nextLine());

                if (amount <= 0) {
                    System.out.println("Amount must be greater than zero.");
                } else {
                    return amount;
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid amount. Enter a valid number.");
            }
        }
    }
    
        

    public static String viewExpenses() {
        if (expenses.isEmpty()) {
            return "No expenses recorded yet.";
        } else 
        
}
