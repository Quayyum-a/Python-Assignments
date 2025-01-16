def calculate_wage(successful_deliveries):
    
    percentage = (successful_deliveries * 100) / 100
    rate = 0

    
    if percentage < 50:
        rate = 160
    elif 50 <= percentage <= 59:
        rate = 250
    elif 60 <= percentage <= 69:
        rate = 400
    elif percentage >= 70:
        rate = 500

    
    total_wage = (successful_deliveries * rate) + 5000
    return total_wage

def main():
    
    successful_deliveries = int(input("Enter the number of successful deliveries: "))
    
    
    print("Wage for the day is:", calculate_wage(successful_deliveries))

if __name__ == "__main__":
    main()
