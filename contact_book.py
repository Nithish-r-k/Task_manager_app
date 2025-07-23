import json

# Step 1: Contact class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


# Step 2: ContactBook class
class ContactBook:
    def __init__(self):
        self.contacts = {}  # Store contacts with name as key

    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("⚠️ Contact with that name already exists!")
        else:
            self.contacts[name] = Contact(name, phone, email)
            print(f"✅ Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("❌ No contacts found!")
        else:
            print("📒 Saved Contacts:")
            for contact in self.contacts.values():
                print(contact)

    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print("🔍 Contact Found:")
            print(contact)
        else:
            print("❌ Contact not found!")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name].phone = phone
            if email:
                self.contacts[name].email = email
            print(f"✅ Contact '{name}' updated successfully!")
        else:
            print("❌ Contact not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"🗑 Contact '{name}' deleted successfully!")
        else:
            print("❌ Contact not found!")

    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as file:
            json.dump({name: vars(contact) for name, contact in self.contacts.items()}, file, indent=4)
        print("💾 Contacts saved to file successfully!")

    def load_from_file(self, filename="contacts.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.contacts = {name: Contact(**info) for name, info in data.items()}
            print("📂 Contacts loaded from file successfully!")
        except FileNotFoundError:
            print("📁 No saved contacts file found. Starting fresh!")


# Step 3: Main menu
def main():
    contact_book = ContactBook()
    contact_book.load_from_file()  # Try loading contacts on startup

    while True:
        print("\n📖 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            contact_book.add_contact(name, phone, email)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            name = input("Enter name to search: ").strip()
            contact_book.search_contact(name)

        elif choice == "4":
            name = input("Enter name to update: ").strip()
            phone = input("Enter new phone (leave blank to keep unchanged): ").strip()
            email = input("Enter new email (leave blank to keep unchanged): ").strip()
            contact_book.update_contact(
                name,
                phone if phone else None,
                email if email else None
            )

        elif choice == "5":
            name = input("Enter name to delete: ").strip()
            contact_book.delete_contact(name)

        elif choice == "6":
            contact_book.save_to_file()
            print("👋 Exiting Contact Book. Have a great day!")
            break

        else:
            print("❌ Invalid option! Please choose from 1 to 6.")

# Run program
if __name__ == "__main__":
    main()
