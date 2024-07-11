contacts= []

def menu():
    print("What you want to do?" )
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

def add_contact():
    name= str(input("Enter the contact's name:"))
    phone= int(input("Enter phone number of contact:"))
    email= str(input("Enter email id of contact:"))
    address= str(input("Enter address of contact:"))
    contact= {"Name": name,"Phone": phone,"Email": email,"Address":address}
    contacts.append(contact)
    print("Contact added successfully!")

def view_all_contacts():
    if contacts:
        print("All Contacts")
        for contact in contacts:
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            print("**********************")
        else:
            print("No contact found.")

def search_contact():
    search_here= input("Enter the name to search contact:")
    found_contacts=[]
    for contact in contacts:
        if search_here.lower() in contact["Name"].lower():
            found_contacts.append(contact)

    if found_contacts:
        print("Contact found:")
        for contact in found_contacts:
            print("Name:", contact["Name"])
            print("Phone:", contact["Phone"])
            print("Email:", contact["Email"])
            print("Address:", contact["Address"])
            print("*********************")
    else:
        print("No contact found!")

def update_contact():
    name= input("Enter the name of contact you want to update:")
    found_contact= None
    for contact in contacts:
        if contact["Name"].lower()== name.lower():
            found_contact= contact
            break
    if found_contact:
        print("Contact found! Enter new details:")
        found_contact["Name"]= input("Enter the new name:")
        found_contact["Phone"]= int(input("Enter the new phone number:"))
        found_contact["Email"]= input("Enter the new email:")
        found_contact["Address"]= input("Enter the new address:")
        print("Contact update successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name= input("Enter the name of the contact you want to delete:")
    for contact in contacts:
        if contact["Name"].lower()== name.lower():
            contacts.remove(contact)
            print("Contact deleted succesfully!")
            break
        else:
            print("Contact not found!")

while True:
    menu()
    choice= input("Enter your choice(1-6):")

    if choice== "1":
        add_contact()
    elif choice== "2":
        view_all_contacts()
    elif choice== "3":
        search_contact()
    elif choice== "4":
        update_contact()
    elif choice== "5":
        delete_contact()
    elif choice== "6":
        print("Exiting......")
        break
    else:
        print("Invalid choice! Please enter from(1-6).")



        

    

