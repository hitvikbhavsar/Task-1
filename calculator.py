
while True:
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    option = input("Choose (1-5): ")

    if option == '5':
        print("Exitedd!")
        break

    try:
        x = float(input("First number: "))
        y = float(input("Second number: "))
    except:
        print("Please enter valid numbers.")
        continue

    if option == '1':
        print("Result:", x + y)
    elif option == '2':
        print("Result:", x - y)
    elif option == '3':
        print("Result:", x * y)
    elif option == '4':
        if y == 0:
            print("Can't divide by zero.")
        else:
            print("Result:", x / y)
    else:
        print("Invalid choice.")
