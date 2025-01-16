from datetime import datetime

class Product:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def get_total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.name:<10} {self.quantity:<5} {self.unit_price:<10} {self.get_total_price():<10}"

def main():
    cart = []
    total_price = 0.0

    customer_count = int(input("How many customers did you attend to? "))

    for _ in range(customer_count):
        customer_name = input("\nWhat is the customer's name: ")

        response = "yes"
        while response.lower() == "yes":
            product_name = input("What did the customer buy: ")
            quantity = int(input("How many pieces: "))
            unit_price = float(input("How much per unit: "))

            product = Product(product_name, quantity, unit_price)
            cart.append(product)
            total_price += product.get_total_price()

            response = input("Add more items? (yes/no): ")

        cashier_name = input("What is the cashier's name: ")
        discount_percentage = float(input("Enter discount percentage (if any): "))

        discount = (discount_percentage / 100) * total_price
        vat = 0.075 * total_price
        final_price = total_price - discount + vat

        
        print("\n<<< SEMICOLON STORE >>>")
        print("MAIN BRANCH")
        print("LOCATION: 312, HERBERT MACAULAY WAY, SABO-YABA, LAGOS")
        print("TEL: 03293828343")
        print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Cashier:", cashier_name)
        print("Customer:", customer_name)

        print(f"\n{'ITEM':<10} {'QTY':<5} {'PRICE':<10} {'TOTAL':<10}")
        for product in cart:
            print(product)

        print("\nSubtotal:", total_price)
        print("Discount: -", discount)
        print("VAT (7.5%): +", vat)
        print("Total:", final_price)

        
        cart.clear()
        total_price = 0.0

if __name__ == "__main__":
    main()
