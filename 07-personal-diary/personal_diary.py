FILE_NAME = "diary.txt"


def add_entry():
    print("\nWrite your diary entry.")
    entry = input("Entry: ").strip()

    if not entry:
        print("Diary entry cannot be empty.")
        return

    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(entry + "\n")

    print("Entry saved successfully.")


def view_entries():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            entries = file.readlines()

        if not entries:
            print("\nNo diary entries found.")
            return

        print("\nDiary Entries")
        print("--------------------")

        for number, entry in enumerate(entries, start=1):
            print(f"{number}. {entry.strip()}")

    except FileNotFoundError:
        print("\nNo diary entries found.")


def search_entries():
    keyword = input("Enter a word to search for: ").strip().lower()

    if not keyword:
        print("Search word cannot be empty.")
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            entries = file.readlines()

        found = False

        for number, entry in enumerate(entries, start=1):
            if keyword in entry.lower():
                print(f"{number}. {entry.strip()}")
                found = True

        if not found:
            print("No matching entries found.")

    except FileNotFoundError:
        print("No diary entries found.")


def delete_all_entries():
    confirmation = input(
        "Are you sure you want to delete all entries? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            file.write("")

        print("All diary entries have been deleted.")
    else:
        print("Nothing was deleted.")


while True:
    print("\nPersonal Diary")
    print("--------------------")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_entry()

    elif choice == "2":
        view_entries()

    elif choice == "3":
        search_entries()

    elif choice == "4":
        delete_all_entries()

    elif choice == "5":
        print("Goodbye.")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")
