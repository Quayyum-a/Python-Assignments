import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class ExpenseTrackerTest {
    @Test
    public void testThatFunctionExists() { 
        ExpenseTracker tracker = new ExpenseTracker();
        String actual = tracker.getHeader();
        String expected = "Welcome to Semicolon Expense Tracker App";  

        assertEquals(expected, actual);
    }
    
    @Test
    public void testThatFunctionGetsMenu() {
        assert ExpenseTracker.getMenu().equals("\n1. Add an expense\n2. View all expenses\n3. Calculate total expenses\n4. Exit");
    }
    
    
    @Test
    public void testThatFunctionReturnsChoiceOne(){
       ExpenseTracker tracker = new ExpenseTracker();
       int actual = tracker.getChoice();
       int expected = 1;
       assertEquals(expected, actual);
    }
    
    @Test
    public void testThatFunctionReturnsChoiceFour(){
       ExpenseTracker tracker = new ExpenseTracker();
       int actual = tracker.getChoice();
       int expected = 4;
       assertEquals(expected, actual);
    }
    
    @Test
    public void testThatFunctionReturnsChoiceInvalid(){
       ExpenseTracker tracker = new ExpenseTracker();
       int actual = tracker.getChoice();
       String expected = "Invalid choice. Please enter a number between 1 and 4.";
       assertEquals(expected, actual);
    }
    
    @Test
    public void testThatFunctionReturnsDate(){
       ExpenseTracker tracker = new ExpenseTracker();
       String actual = tracker.getDate();
       String expected = "2023-04-12";
       assertEquals(expected, actual);
    }
    
    @Test
    public void testThatFunctionReturnsDescription(){
        ExpenseTracker tracker = new ExpenseTracker();
        String actual = tracker.getDescription();
        String expected = "Buy groceries";
        assertEquals(expected, actual);
    }
    
    @Test
    public void testThatFunctionReturnsAmount(){
        ExpenseTracker tracker = new ExpenseTracker();
        double actual = tracker.getAmount();
        double expected = 2000.00;
        assertEquals(expected, actual);
    }
    
    @Test
    
}

