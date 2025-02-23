
import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x650")
        self.root.configure(bg="lightgreen")  

        self.contacts = {}  # Dictionary to store contacts
        self.filename = "contacts.json"
        self.load_contacts()  # Load contacts from JSON file on startup

        # Creating input fields (Name, Phone, Address, Email)
        tk.Label(self.root, text="Name:", bg="violet").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Phone:", bg="blue").pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        tk.Label(self.root, text="Address:", bg="white").pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack()

        tk.Label(self.root, text="Email:", bg="orange").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()

        # Buttons for different operations
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, bg="green", fg="white")
        self.add_button.pack()

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact, bg="blue", fg="white")
        self.update_button.pack()

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact, bg="yellow")
        self.search_button.pack()

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, bg="red", fg="white")
        self.delete_button.pack()

        # Contact list display (Treeview table)
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Address", "Email"), show='headings')
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Email", text="Email")
        self.tree.pack()

        self.refresh_contacts()  # Display contacts

    def save_contacts(self):
        """ Saves contacts to a JSON file """
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def load_contacts(self):
        """ Loads contacts from a JSON file if it exists """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    self.contacts = json.load(file)
                except json.JSONDecodeError:
                    self.contacts = {}  # Reset if the file is corrupted

    def add_contact(self):
        """ Adds a new contact and saves it to JSON """
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()

        if name and phone and address and email:
            self.contacts[name] = {'Phone': phone, 'Address': address, 'Email': email}
            self.save_contacts()  # Save to JSON
            self.refresh_contacts()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def search_contact(self):
        """ Searches for a contact by name """
        name = self.name_entry.get()
        if name in self.contacts:
            contact = self.contacts[name]
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {contact.get('Phone', 'N/A')}\n"
                                                 f"Address: {contact.get('Address', 'N/A')}\nEmail: {contact.get('Email', 'N/A')}")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def update_contact(self):
        """ Updates an existing contact and saves changes to JSON """
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        email = self.email_entry.get()

        if name in self.contacts:
            self.contacts[name] = {'Phone': phone, 'Address': address, 'Email': email}
            self.save_contacts()  # Save to JSON
            self.refresh_contacts()
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def delete_contact(self):
        """ Deletes a contact and updates JSON """
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()  # Save to JSON
            self.refresh_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def refresh_contacts(self):
        """ Clears the table and updates the displayed contacts safely """
        for item in self.tree.get_children():
            self.tree.delete(item)

        for name, details in self.contacts.items():
            phone = details.get('Phone', "N/A")  # Default to "N/A" if missing
            address = details.get('Address', "N/A")  # Default to "N/A" if missing
            email = details.get('Email', "N/A")  # Default to "N/A" if missing

            self.tree.insert("", tk.END, values=(name, phone, address, email))

# Running the application
if __name__ == "__main__":
    root = tk.Tk()
    ContactBook(root)
    root.mainloop()
