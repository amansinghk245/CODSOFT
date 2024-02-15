# Purpose: CONTACT BOOK
# Author: Aman Kumar Singh

import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contact_book = {}

        # Create GUI components
        self.label_name = tk.Label(root, text="Name:")
        self.label_phone = tk.Label(root, text="Phone Number:")

        self.entry_name = tk.Entry(root)
        self.entry_phone = tk.Entry(root)

        self.button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.button_display = tk.Button(root, text="View Contact List", command=self.display_contacts)
        self.button_search = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.button_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.button_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Layout components
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.label_phone.grid(row=1, column=0, padx=10, pady=5)

        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.button_add.grid(row=2, column=0, columnspan=2, pady=10)
        self.button_display.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_search.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_update.grid(row=5, column=0, columnspan=2, pady=10)
        self.button_delete.grid(row=6, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone.get()

        if name and phone_number:
            if name not in self.contact_book:
                self.contact_book[name] = phone_number
                messagebox.showinfo("Success", f"Contact {name} added successfully!")
                self.clear_entries()
            else:
                messagebox.showwarning("Error", f"Contact {name} already exists. Use 'Update Contact' to modify.")
        else:
            messagebox.showwarning("Error", "Please enter both name and phone number.")

    def display_contacts(self):
        if not self.contact_book:
            messagebox.showinfo("Info", "No contacts found.")
        else:
            contacts = "\n".join(f"{name}: {phone}" for name, phone in self.contact_book.items())
            messagebox.showinfo("Contacts", contacts)

    def search_contact(self):
        name = self.entry_name.get()
        if name in self.contact_book:
            messagebox.showinfo("Contact Found", f"Phone number for {name}: {self.contact_book[name]}")
        else:
            messagebox.showwarning("Contact Not Found", f"No contact found for {name}.")

    def update_contact(self):
        name = self.entry_name.get()
        phone_number = self.entry_phone.get()

        if name in self.contact_book:
            self.contact_book[name] = phone_number
            messagebox.showinfo("Success", f"Contact {name} updated successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", f"No contact found for {name}. Use 'Add Contact' to create a new contact.")

    def delete_contact(self):
        name = self.entry_name.get()

        if name in self.contact_book:
            del self.contact_book[name]
            messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", f"No contact found for {name}.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
