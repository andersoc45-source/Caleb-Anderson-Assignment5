# contact_manager.py

contacts = {}

class DuplicateContactError(Exception):
    """ Custom exception for duplicate contacts. """
    def __init__(self, message="Duplicate contacts found."):
        self.message = message
        super().__init__(self.message)

def add_contact(name, phone, dict):
    """
        Adds name as a key and phone as a value to the dictionary parameter.
        Raises an error if the contact is already present.
        
        Args:
            name (string): The name of the contact.
            phone (string): The phone number of the contact.
            dict (dictionary): A dictionary the contact information is being added to.
            
        Returns:
            None
    """
    if name in dict:
        raise DuplicateContactError(f"{name} is already in contacts.")
    
    dict[name] = phone
    print(f"Added {name} to contacts.")

def find_contact(name, dict):
    """
        Finds the phone number of the given contact name.
        
        Args:
            name (string): The name of the contact.
            dict (dictionary): A dictionary the contact neme is searched for.
            
        Returns:
            string: The phone number of the given contact name.
            None: If no match is found.
    """
    try:
        print(dict[name])
        return dict[name]
    except KeyError:
        print("Contact not found.")

def delete_contact(name, dict):
    """
        Deletes a contact from a given dictionary with a name.
        
        Args:
            name (string): The name of the contact.
            dict (dictionary): A dictionary the contact is being deleted from.
            
        Returns:
            None
    """
    try:
        del dict[name]
        print(f"Deleted {name}.")
    except KeyError:
        print("Contact not found.")

def main():
    while True: # Loops until the user enters 4.
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice) # converts choice to a number.

            if choice == 1: # Add contact
                name = input("Enter contact name: ")
                phone = input("Enter phone number: ")

                try:
                    add_contact(name, phone, contacts)
                except DuplicateContactError as e:
                    print(f"Add contact failed: {e}") # Prints if the user tried to enter a duplicate contact.

            elif choice == 2: # Find contact
                name = input("Enter name to find: ")
                find_contact(name, contacts)
            elif choice == 3: # Delete contact
                name = input("Enter name to delete: ")
                delete_contact(name, contacts)
            elif choice != 4:
                print("Invalid choice.") # Prints if the user entered a number that was not a listed option.
        except ValueError:
            print("Not an integer. Enter a valid number.") # Prints if the user entered something othar than a number.
        if choice == 4:
            break

if __name__ == "__main__":
    main()