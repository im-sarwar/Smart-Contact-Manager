import Add_Contacts
import view_contacts
import search_contacts
import update_contact
import delete_contact

def choice():
    while True:
    
        user_choice = input("    ------------    "
        "\nDo you want to "
        "\n1.Add Contacts"
        "\n2.View Contacts"
        "\n3.Search Contacts" \
        "\n4.Edit/Update Contacts" \
        "\n5.Delete Contacts" \
        "\n6.Exit Now").strip()

        while user_choice not in('1', '2', '3', '4', '5', '6'):

            print("Enter Valid Choice Please:")
            user_choice = input("-----------------"
            "\nDo you want to "
            "\n1.Add Contacts"
            "\n2.View Contacts"
            "\n3.Search Contacts" \
            "\n4.Edit/Update Contacts" \
            "\n5.Delete Contacts" \
            "\n6.Exit Now").strip()
    
            
        if user_choice=='1':
            Add_Contacts.Add_contacts()
        elif user_choice=='2':
            view_contacts.view_contacts()
        elif user_choice=='3':
            search_contacts.search_contact()
        elif user_choice=='4':
            update_contact.update_contact()
        elif user_choice=='5':
            delete_contact.delete_contacts()
        elif user_choice=='6':
            print("Exited")
            exit()


choice()