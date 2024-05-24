class Person:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.add_default_contacts()
        self.display_menu()

    def add(self, person):
        self.contacts.append(person)
        print("Contact added.")
        self.display_menu()

    def show_all(self):
        for person in self.contacts:
            print(f"Name: {person.name}, Phone: {person.phone}, Email: {person.email}, Address: {person.address}")
        self.display_menu()

    def search(self, keyword):
        results = []
        for person in self.contacts:
            if keyword.lower() in person.name.lower() or keyword in person.phone:
                results.append(person)
        if results:
            print("Search results:")
            for person in results:
                print(f"Name: {person.name}, Phone: {person.phone}, Email: {person.email}, Address: {person.address}")
        else:
            print("No matching contacts.")
        self.display_menu()

    def update(self, old_person, new_person):
        index = self.contacts.index(old_person)
        self.contacts[index] = new_person
        print("Contact updated.")
        self.display_menu()

    def delete(self, person):
        self.contacts.remove(person)
        print("Contact deleted.")
        self.display_menu()

    def display_menu(self):
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            person = Person(name, phone, email, address)
            self.add(person)

        elif choice == "2":
            self.show_all()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            self.search(keyword)

        elif choice == "4":
            old_name = input("Enter name of contact to update: ")
            old_phone = input("Enter phone number of contact to update: ")
            results = self.search(old_name) + self.search(old_phone)
            if results:
                print("Select contact to update:")
                for i, person in enumerate(results):
                    print(f"{i+1}. Name: {person.name}, Phone: {person.phone}")
                index = int(input("Enter index of contact to update: ")) - 1
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email: ")
                new_address = input("Enter new address: ")
                new_person = Person(new_name, new_phone, new_email, new_address)
                self.update(results[index], new_person)
            else:
                print("Contact not found.")

        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            phone = input("Enter phone number of contact to delete: ")
            results = self.search(name) + self.search(phone)
            if results:
                print("Select contact to delete:")
                for i, person in enumerate(results):
                    print(f"{i+1}. Name: {person.name}, Phone: {person.phone}")
                index = int(input("Enter index of contact to delete: ")) - 1
                self.delete(results[index])
            else:
                print("Contact not found.")

        elif choice == "6":
            print("Exiting...")
            exit()

        else:
            print("Invalid choice.")
            self.display_menu()

    def add_default_contacts(self):
        self.add(Person("Codsoft", "1234567890", "contact@codsoft.in", "INDIA"))
        self.add(Person("Dhiraj Rajai", "9016022011", "dhirajrajai12@gmail.com", "Bhavnagar, Gujarat"))
        self.add(Person("Internship", "1111111111", "intern@example.com", "Batch A48"))

ContactManager()
