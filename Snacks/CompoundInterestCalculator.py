def calculate_compound_interest(principal, monthly_contribution, annual_rate, years, compound_frequency):
    amount = principal * (1 + annual_rate / compound_frequency) ** (compound_frequency * years)
    for count in range(1, years * 12 + 1):
        amount += monthly_contribution * (1 + annual_rate / compound_frequency) ** (compound_frequency * (years - (count / 12.0)))
    return amount
    
    
def main():
    
     principal = float(input("Enter your initial investment: "))
     if principal < 0:
        print("Principal cannot be negative.")
        return
    
     monthly_contribution = float(input("Enter your monthly contribution: "))
     if monthly_contribution < 0:
        print("Monthly contribution cannot be negative.")
        return
    
     years = int(input("Enter length of time in years: "))
     if years <= 0:
         print("Years must be a positive integer.")
         return
     
     annual_rate = float(input("Enter the estimated annual interest rate (in %): "))
     if annual_rate <= 0:
         print("Interest rate must be positive.")
         return
     
     variance_range = float(input("Enter a variance range (not used in calculation): "))
     if variance_range < 0:
        print("Variance range cannot be negative.")
        return
    
     print("\nSelect Compounding Frequency: ")
     print("1. Annually")
     print("2. Quarterly")
     print("3. Monthly")
     print("4. Weekly")
     print("5. Daily")
    
     try:
        response = int(input("Enter a choice: "))
     except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        return
    
     match response:
        case 1:
            compound_frequency = 1
        case 2:
            compound_frequency = 4
        case 3:
            compound_frequency = 12
        case 4:
            compound_frequency = 52
        case 5:
            compound_frequency = 365
        case _:
            print("Invalid choice. Please select a number between 1 and 5.")
            return
        
        
        
     future_investment_value = calculate_compound_interest(principal, monthly_contribution, annual_rate / 100, years, compound_frequency)
     print(f"\nFuture Investment Value after {years} years = {future_investment_value:.2f}")
    
if __name__ == "__main__":
    main()