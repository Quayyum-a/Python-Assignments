total = 0

numoftransactions = int(input("How many transactions do you want to perform? "))

for _ in range(numoftransactions):
    print("\nEnter 1 for Deposit 2 for Withdraw")

    response = int(input())

    match response:
        case 1:
            print("Deposit")
            deposit = int(input("\nEnter the amount to deposit: "))
            total += deposit
            print(f"Money deposited is : {deposit}. Total balance is now {total}.")

        case 2:
            print("Withdraw")
            withdraw = int(input("\nEnter the amount to withdraw: "))
            if withdraw > total:
                print("Insufficient funds! No money!!!.")
            else:
                total -= withdraw
                print(f"Money has been withdrawn, new balance is {total}")

        case _:
            print("Exit transaction")