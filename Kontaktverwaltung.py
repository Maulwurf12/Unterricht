import json

class contact:
    def __init__(self, firstname, lastname, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def con_to_dic(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'phone': self.phone
        }

class main:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()
        decision = input("""What would you like to do?
        1. add contact
        2. remove contact
        3. edit contact
        4. show contacts
        5. exit""")
        if decision == '1':
            pre_name = input("What shall the pre name be?")
            last_name = input("What shall the last name be?")
            email = input("What is the email address?")
            phone = input("What is the phone number?")
            self.add_contact(pre_name, last_name, email, phone)
        elif decision == '2':
            print("You want to delete a contact? type Y(Yes) or N(No)")
            y_n_decision = input()
            if y_n_decision == 'Y':
                pre_name = input("Type in the pre_name of the person you want to delete?")
                last_name = input("Type in the last name of the person you want to delete?")
                full_name = pre_name + " " + last_name
                self.remove_contact(full_name)
            elif y_n_decision == 'N':
                print("Nothing will be deleted.")
        elif decision == '3':
            pre_name = input("Type in the pre_name of the person you want to edit?")
            last_name = input("Type in the last name of the person you want to edit?")
            full_name = pre_name + " " + last_name
            self.edit_contact(full_name)
        elif decision == '4':
            self.show_contacts()
        elif decision == '5':
            print("Exiting...")
            exit(0)
        else:
            print("You chose an invalid choice")

    def add_contact(self, pre_name, last_name, email, phone):
        con = contact(pre_name, last_name, email, phone)
        full_name = pre_name + " " + last_name
        self.contacts[full_name] = con
        self.write_contacts()

    def remove_contact(self, full_name):
        if full_name in self.contacts:
            del self.contacts[full_name]
            self.write_contacts()
            print(f"Contact {full_name} removed.")
        else:
            print(f"Contact {full_name} not found.")

    def show_contacts(self):
        if self.contacts:
            for full_name, con in self.contacts.items():
                print(f"{full_name}: {con.get_email()} - {con.get_phone()}")
        else:
            print("No contacts available.")

    def load_contacts(self):
        print("Loading contacts...")
        try:
            with open('contacts.json', 'r') as file:
                contacts_data = json.load(file)
            for full_name, contact_data in contacts_data.items():
                con = contact(contact_data['firstname'], contact_data['lastname'],
                              contact_data['email'], contact_data['phone'])
                self.contacts[full_name] = con
            print("Contacts loaded successfully.")
        except FileNotFoundError:
            print("No contact file found. Starting with an empty contact list.")
        except json.JSONDecodeError:
            print("Error decoding the contact file. It may be corrupted.")

    def write_contacts(self):
        print("Saving contacts...")
        serializable_dict = {key: value.con_to_dic() for key, value in self.contacts.items()}
        with open('contacts.json', 'w') as file:
            json.dump(serializable_dict, file, indent=4)

    def edit_contact(self, full_name):
        if full_name in self.contacts:
            con = self.contacts[full_name]
            print(f"Editing contact: {full_name}")
            edit_decision = input("""What would you like to edit:
            (1) pre-name
            (2) last-name
            (3) email
            (4) phone
            """)
            old_firstname = con.get_firstname()
            old_lastname = con.get_lastname()

            if edit_decision == '1':
                pre_name = input("Type in the new pre-name of your contact: ")
                con.firstname = pre_name
            elif edit_decision == '2':
                last_name = input("Type in the new last name of your contact: ")
                con.lastname = last_name
            elif edit_decision == '3':
                email = input("Type in the new email of your contact: ")
                con.email = email
            elif edit_decision == '4':
                phone = input("Type in the new phone number of your contact: ")
                con.phone = phone
            if con.get_firstname() != old_firstname or con.get_lastname() != old_lastname:
                new_full_name = con.get_firstname() + " " + con.get_lastname()
                del self.contacts[full_name]
                self.contacts[new_full_name] = con
                print(f"Name updated to: {new_full_name}")

            self.write_contacts()
        else:
            print(f"Contact {full_name} not found.")


if __name__ == "__main__":
    while True:
        app = main()
