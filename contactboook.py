   
class ContactBook:
    def __init__(self):
        self.contacts = {} # create an empty dictionary where we can store contact

    def add_contact(self, name, phone, address, email):
        if name and phone and address and email:
            self.contacts[name] = {'Phone': phone, 'Address': address, 'Email': email}
            print("\n Contact added successfully!")
        else:
            print("\n Error: All fields are required!")

    def search_contact(self, name):
        if name in self.contacts:#it shows the details like phone address email of the user
            contact = self.contacts[name]
            print("\n Contact Found:")
            print(f"Name: {name}\n Phone: {contact['Phone']}\n Address: {contact['Address']}\n Email: {contact['Email']}")
        else:
            print("\n Error: Contact not found!")

    def update_contact(self, name, phone, address, email):
        if name in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Address': address, 'Email': email}
            print("\n Contact updated successfully!")
        else:
            print("\n Error: Contact not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("\n Contact deleted successfully!")
        else:
            print("\n Error: Contact not found!")

    def display_contacts(self):
        """ Always displays contacts after each operation """
        if not self.contacts:
            print("\n No contacts available.")
        else:
            print("\n Contact List:")
            for name, details in self.contacts.items():
                print(f"\n Name: {name}\n Phone: {details['Phone']}\n Address: {details['Address']}\n Email: {details['Email']}\n" + "-" * 30)


if __name__ == "__main__":
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1️ Add Contact")
        print("2️ Search Contact")
        print("3️ Update Contact")
        print("4️ Delete Contact")
        print("5️ Display Contacts")
        print("6️ Exit")

        choice = input(" Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            address = input("Enter Address: ")
            email = input("Enter Email: ")
            contact_book.add_contact(name, phone, address, email)
            contact_book.display_contacts()  

        elif choice == "2":
            name = input("Enter Name to search: ")
            contact_book.search_contact(name)

        elif choice == "3":
            name = input("Enter Name to update: ")
            phone = input("Enter new Phone: ")
            address = input("Enter new Address: ")
            email = input("Enter new Email: ")
            contact_book.update_contact(name, phone, address, email)
            contact_book.display_contacts()  # Show contacts after updating all the essentaial things

        elif choice == "4":
            name = input("Enter Name to delete: ")
            contact_book.delete_contact(name)
            contact_book.display_contacts()  # Show contacts after deletion 

        elif choice == "5":
            contact_book.display_contacts()

        elif choice == "6":
            print("\n Exiting Contact Book...")
            input("Press Enter to exit...")  # Keeps window open until user presses Enter key 
            break

        else:
            print("\n Invalid choice! Please enter a valid option.")

        input("\nPress Enter to continue...")  # Keeps output visible before refreshing 