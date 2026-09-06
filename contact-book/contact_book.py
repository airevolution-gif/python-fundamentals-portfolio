contacts = {}


def add_contact():
    name = input("Enter contact name: ").strip()

    if name in contacts:
        print("That contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List")
    print("--------------------")

    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print("--------------------")


def search_contact():
    name = input("Enter the name to search: ").strip()

    if name in contacts:
        print("\nContact Found")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter the name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email address: ").strip()

    contacts[name]["phone"] = phone
    contacts[name]["email"] = email

    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter the name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


while True:
    print("\nContact Book")
    print("--------------------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thanks for using the Contact Book.")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 6.")
