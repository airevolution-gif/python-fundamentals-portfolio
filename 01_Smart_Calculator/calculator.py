# Smart Calculator Pro
# Created by Haider Sultan
# Python Fundamentals Portfolio

import math
from colorama import Fore, Style, init
from pyfiglet import figlet_format

init(autoreset=True)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def power(a, b):
    return a ** b


def modulus(a, b):
    if b == 0:
        return "Error: Cannot use zero as the divisor."
    return a % b


def square_root(a):
    if a < 0:
        return "Error: Cannot find the square root of a negative number."
    return math.sqrt(a)


def factorial(a):
    if a < 0 or not a.is_integer():
        return "Error: Factorial requires a non-negative whole number."
    return math.factorial(int(a))


def calculator():
    print(Fore.CYAN + figlet_format("Smart Calculator"))
    print(Fore.YELLOW + "Created by Haider Sultan")
    print(Fore.GREEN + "Python Fundamentals Portfolio")
    print("-" * 50)

    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Factorial")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == "9":
            print(Fore.GREEN + "\nThank you for using Smart Calculator!")
            break

        try:
            if choice in ["1", "2", "3", "4", "5", "6"]:
                first = float(input("Enter first number: "))
                second = float(input("Enter second number: "))

                if choice == "1":
                    result = add(first, second)
                elif choice == "2":
                    result = subtract(first, second)
                elif choice == "3":
                    result = multiply(first, second)
                elif choice == "4":
                    result = divide(first, second)
                elif choice == "5":
                    result = power(first, second)
                elif choice == "6":
                    result = modulus(first, second)

            elif choice == "7":
                number = float(input("Enter a number: "))
                result = square_root(number)

            elif choice == "8":
                number = float(input("Enter a whole number: "))
                result = factorial(number)

            else:
                print(Fore.RED + "Invalid choice. Please choose 1-9.")
                continue

            print(Fore.CYAN + f"\nResult: {result}")

        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")


if __name__ == "__main__":
    calculator()
