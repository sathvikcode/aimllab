balance = 25000

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Exit")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        amount = float(input("Deposit Amount: "))
        balance += amount
        print("Updated Balance:", balance)
    elif choice == 2:
        amount = float(input("Withdraw Amount: "))
        if amount <= balance:
            balance -= amount
            print("Collect Cash")
            print("Balance:", balance)
        else:
            print("Insufficient Balance")
    elif choice == 3:
        print("Current Balance:", balance)
    elif choice == 4:
        print("Thank You")
        break
    else:
        print("Invalid Choice")
