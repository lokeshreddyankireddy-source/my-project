print("welcome to mini calculator")
while True :
    print("\n options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("enter your choice")
    if choice == "5":
        print("calcutator stopped successfully")
        break
    num1 = float(input("enter first number"))
    num2 = float(input("enter second number"))
    if choice == "1":
        result = num1 + num2
        print(f"answer: {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"answer: {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"answer: {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"answer: {result}")
        else:
            print("error: division by zero")
    else:
        print("invalid choice, please try again")