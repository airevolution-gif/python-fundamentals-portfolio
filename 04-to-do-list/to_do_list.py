tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks added yet.")
        return

    print("\nYour Tasks")
    print("--------------------")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def add_task():
    task = input("Enter a new task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def remove_task():
    if not tasks:
        print("There are no tasks to remove.")
        return

    show_tasks()

    try:
        number = int(input("Enter the task number to remove: "))

        if 1 <= number <= len(tasks):
            removed_task = tasks.pop(number - 1)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def clear_tasks():
    if not tasks:
        print("There are no tasks to clear.")
        return

    confirmation = input("Are you sure you want to clear all tasks? (yes/no): ")

    if confirmation.lower() == "yes":
        tasks.clear()
        print("All tasks have been removed.")
    else:
        print("Tasks were not removed.")


while True:
    print("\nTo-Do List")
    print("--------------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        clear_tasks()

    elif choice == "5":
        print("Thanks for using the To-Do List.")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
