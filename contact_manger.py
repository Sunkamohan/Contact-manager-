import json
import os

# Define the path to the contacts file
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """
    Load contacts from the JSON file.

    This function checks if the contacts file exists. If it does, it opens the file and loads the contacts into a list.
    If the file does not exist, it returns an empty list.

    Returns:
        list: A list of dictionaries where each dictionary represents a contact.
    """
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    """
    Save the contacts to the JSON file.

    This function takes a list of contacts and saves it to the contacts file in JSON format.

    Args:
        contacts (list): A list of dictionaries where each dictionary represents a contact.
    """
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email):
    """
    Add a new contact to the contacts list and save it to the file.

    This function creates a new contact dictionary with the provided name, phone, and email.
    It then loads the existing contacts, adds the new contact, and saves the updated contacts list.

    Args:
        name (str): The name of the contact.
        phone (str): The phone number of the contact.
        email (str): The email address of the contact.
    """
    contacts = load_contacts()
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def delete_contact(name):
    """
    Delete a contact by name from the contacts list and save the changes to the file.

    This function searches for a contact by name in the contacts list and removes it if found.
    It then saves the updated contacts list.

    Args:
        name (str): The name of the contact to delete.
    """
    contacts = load_contacts()
    contacts = [contact for contact in contacts if contact['name'] != name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully.")

def search_contact(name):
    """
    Search for a contact by name and print the details if found.

    This function searches for a contact by name in the contacts list.
    If the contact is found, it prints the contact details.
    If not, it prints a message saying the contact was not found.

    Args:
        name (str): The name of the contact to search for.
    """
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Contact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print(f"Contact '{name}' not found.")

def list_contacts():
    """
    List all contacts and print their details.

    This function loads all the contacts from the contacts file and prints each contact's details.
    If no contacts are found, it prints a message saying no contacts were found.
    """
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 20)

def main():
    """
    Main function to run the contact manager application.

    This function displays a menu with options to add, delete, search, list contacts, or exit the application.
    It handles user input and calls the appropriate functions based on the user's choice.
    """
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. List Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '3':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print("Exiting Contact Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
