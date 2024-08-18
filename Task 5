import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        
        self.contacts = []
        
        self.create_widgets()

    def create_widgets(self):
        # Add Contact
        tk.Label(self.root, text="Add New Contact").grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Name").grid(row=1, column=0, sticky=tk.E)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Phone").grid(row=2, column=0, sticky=tk.E)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Email").grid(row=3, column=0, sticky=tk.E)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=3, column=1)

        tk.Label(self.root, text="Address").grid(row=4, column=0, sticky=tk.E)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=4, column=1)

        tk.Button(self.root, text="Add Contact", command=self.add_contact).grid(row=5, column=0, columnspan=2, pady=10)
        
        # View Contacts
        tk.Label(self.root, text="Contacts List").grid(row=6, column=0, columnspan=2, pady=10)
        
        self.contact_listbox = tk.Listbox(self.root, width=50)
        self.contact_listbox.grid(row=7, column=0, columnspan=2)
        self.contact_listbox.bind('<<ListboxSelect>>', self.on_select)

        tk.Button(self.root, text="View Contact", command=self.view_contact).grid(row=8, column=0)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).grid(row=8, column=1)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).grid(row=9, column=0, columnspan=2, pady=10)

        # Search Contacts
        tk.Label(self.root, text="Search Contact").grid(row=10, column=0, columnspan=2, pady=10)

        tk.Label(self.root, text="Search by Name or Phone").grid(row=11, column=0, sticky=tk.E)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=11, column=1)

        tk.Button(self.root, text="Search", command=self.search_contact).grid(row=12, column=0, columnspan=2, pady=10)
    
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            self.update_contact_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Input Error", "Name and phone are required fields.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def on_select(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            self.selected_contact = self.contacts[selected_index[0]]

    def view_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            messagebox.showinfo("Contact Details", f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to view.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            new_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact.name)
            new_phone = simpledialog.askstring("Update Contact", "Enter new phone:", initialvalue=contact.phone)
            new_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact.email)
            new_address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact.address)

            if new_name and new_phone:
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                self.update_contact_listbox()
            else:
                messagebox.showwarning("Input Error", "Name and phone are required fields.")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            if messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {contact.name}?"):
                del self.contacts[selected_index[0]]
                self.update_contact_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete.")

    def search_contact(self):
        search_term = self.search_entry.get().lower()
        if search_term:
            matching_contacts = [contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone]
            if matching_contacts:
                result = "\n\n".join([f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}" for contact in matching_contacts])
                messagebox.showinfo("Search Results", result)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name or phone number to search.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
