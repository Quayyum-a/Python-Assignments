today = int(input("Enter today's day: "))

future = int(input("Enter the number of days elapsed since today: "))

future_day = (today + future) % 7

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(f"Today is {days_of_week[today]} and the future day is {days_of_week[future_day]}")
