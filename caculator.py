def addition(number1, number2):
    return number1 + number2
def substraction(number1, number2):
    return number1 - number2
def division(number1, number2):
    return number1 / number2
def modulus(number1, number2):
    return number1 % number2
def actual_system():
    print("<<<<<<< Welcome to the Shani Ahmad Calculator >>>>>>>>")
    number1 = int(input("Enter your first Number: "))
    number2 = int(input("Enter your second Number: "))
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Modulus")
        print("5. Exit")
        number = input("Enter your choice: ")
        if number == "1":
            print("Result:", addition(number1, number2))
        elif number == "2":
            print("Result:", substraction(number1, number2))
        elif number == "3":
            print("Result:", division(number1, number2))
        elif number == "4":
            print("Result:", modulus(number1, number2))
        elif number == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
actual_system()
print("new feature in master branch")