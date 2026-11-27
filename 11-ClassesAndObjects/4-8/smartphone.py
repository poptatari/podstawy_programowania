from contact import Contact
from contact_list import Contact_List


def main():
    # Create an object representing a contact list
    smartphone_contacts = Contact_List()

    # Add contacts
    smartphone_contacts.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    smartphone_contacts.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    smartphone_contacts.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    smartphone_contacts.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    # Display the contact list available on the smartphone
    smartphone_contacts.display_contacts()


if __name__ == "__main__":
    main()