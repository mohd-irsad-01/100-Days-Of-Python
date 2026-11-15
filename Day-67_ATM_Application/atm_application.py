print("--- WELCOME TO PYTHON ATM ---")

balance = 5000
pin = 1234
transactions = []

user_pin = int(input("Enter your PIN: "))
if user_pin == pin:
    while True:

        print("\n=== ATM MENU ===")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdrow Money")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("Your Balance: Rs.", balance)
        elif choice == "2":
            amount = int(input("Enter deposet amount: "))
            if amount > 0:
                balance += amount
                transactions.append("Deposited: Rs. " + str(amount))
                print("Money Deposited Successfully")
            else:
                print("Invalid Amount")
        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Invalid Amount")
            elif amount <= balance:
                balance -= amount
                transactions.append("Withdrawan: Rs." + str(amount))
                print("Please collect your cash")
            else:
                print("Insufficient Balance")
        elif choice == "4":
            print("=== MINI STATEMENT ===")
            if len(transactions) == 0:
                print("No Transactions Yet")
            else:
                for transaction in transactions:
                    print(transaction)
            print("Available Balance: Rs.", balance)
        elif choice == "5":
            print("Thank you for using Python ATM!")
            break
        else:
            print("Invalid Choice, Try Again")
else:
    print("Incorrect PIN! Access Denied.")
