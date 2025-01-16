def main():
 sapa = 4
 small = 6
 big = 8
 odogwu = 12

 print("""
 Pizza Type      Number Of Slices    Price Per Box
 Sapa size           4             2,500
 Small money         6             2,900
 Big boys            8             4,000
 Odogwu              12            5,200
 """)

 number_of_people = int(input("Number of People = "))
 pizza_type = input("Pizza Type = ").strip()

 if pizza_type.lower() == "sapa size":
     num_of_boxes = (number_of_people + sapa - 1) // sapa
     left_over = num_of_boxes * sapa - number_of_people
     cost = num_of_boxes * 2500
     print(f"\nBoxes to buy: {num_of_boxes}")
     print(f"Left over is: {left_over}")
     print(f"Total Cost is = {cost}")

 elif pizza_type.lower() == "small money":
     num_of_boxes = (number_of_people + small - 1) // small
     left_over = num_of_boxes * small - number_of_people
     cost = num_of_boxes * 2900
     print(f"\nBoxes to buy: {num_of_boxes}")
     print(f"Left over is: {left_over}")
     print(f"Total Cost is = {cost}")

 elif pizza_type.lower() == "big boys":
     num_of_boxes = (number_of_people + big - 1) // big
     left_over = num_of_boxes * big - number_of_people
     cost = num_of_boxes * 4000
     print(f"\nBoxes to buy: {num_of_boxes}")
     print(f"Left over is: {left_over}")
     print(f"Total Cost is = {cost}")

 elif pizza_type.lower() == "odogwu":
     num_of_boxes = (number_of_people + odogwu - 1) // odogwu
     left_over = num_of_boxes * odogwu - number_of_people
     cost = num_of_boxes * 5200
     print(f"\nBoxes to buy: {num_of_boxes}")
     print(f"Left over is: {left_over}")
     print(f"Total Cost is = {cost}")
 
 else:
     print("Invalid pizza type entered!")

if __name__ == "__main__":
    main()

