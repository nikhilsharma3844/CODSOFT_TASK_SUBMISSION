def calculator():
    print("Simple Calculator")
    print("=================")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose the operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            operation = '+'
        elif choice == '2':
            result = num1 - num2
            operation = '-'
        elif choice == '3':
            result = num1 * num2
            operation = '*'
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
            operation = '/'
        else:
            print("Invalid operation choice!")
            return

        print(f"\nResult: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Run the calculator
calculator()
