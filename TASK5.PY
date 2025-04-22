contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone to search: ").strip().lower()
    found = False
    for c in contacts:
        if keyword in c["name"].lower() or keyword in c["phone"]:
            print(f"\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == name:
            print("Leave blank to keep current value.")
            c["phone"] = input(f"New Phone ({c['phone']}): ") or c["phone"]
            c["email"] = input(f"New Email ({c['email']}): ") or c["email"]
            c["address"] = input(f"New Address ({c['address']}): ") or c["address"]
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == name:
            contacts.remove(c)
            print("Contact deleted.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\n==== Contact Manager ====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

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
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
