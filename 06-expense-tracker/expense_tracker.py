expenses = []


def add_expense():
    description = input("Enter expense description: ").strip()

    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount > 0:
                break

            print("Amount must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter expense category: ").strip()

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\nExpenses")
    print("--------------------")

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']}")
        print(f"   Amount: ${expense['amount']:.2f}")
        print(f"   Category: {expense['category']}")


def show_total():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal expenses: ${total:.2f}")


def show_category_total():
    if not expenses:
        print("No expenses recorded.")
        return

    category = input("Enter category: ").strip().lower()

    total = 0

    for expense in expenses:
        if expense["category"].lower() == category:
            total += expense["amount"]

    print(f"Total spent on {category}: ${total:.2f}")


def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\nExpense Tracker")
    print("--------------------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Show Category Total")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        show_category_total()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Thanks for using the Expense Tracker.")
        break

    else:
        print("Invalid choice. Please select 1 to 6.")
