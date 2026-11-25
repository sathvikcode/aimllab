import calculator

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result =", calculator.add(a, b))
elif choice == 2:
    print("Result =", calculator.subtract(a, b))
elif choice == 3:
    print("Result =", calculator.multiply(a, b))
elif choice == 4:
    print("Result =", calculator.divide(a, b))
else:
    print("Invalid Choice!")
