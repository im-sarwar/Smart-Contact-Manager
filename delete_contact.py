import json

def delete_contacts():
    try:
        with open("contacts_book.json") as f:
            contacts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Contacts Exist.")
        exit()
    
    while True:
        choice = input("1.Delete all contacts:"
        "\n2. Delete one specfic contact." \
        "\n-----------" \
        "\nEnter Your Choice:")

        if choice not in("1" , "2"):
            print("Please Enter Valid Choice")
        else:
            if choice=="1":
                confirm = input("Enter C to confirm, enter anyother key to go to main menu:").strip().lower()
                if confirm=="c":
                    with open("contacts_book.json" , "w") as f:
                        pass
                    print("All Contacts Deleted.")
                    return
                else:
                    return
                
            elif choice=='2':
                dlt = input("Enter the contact you want to Delete:")
                if contacts.get(dlt)==None:
                    print(f"{dlt} isn't already saved.")
                    return
                else:
                    contacts.pop(dlt)
                    with open("contacts_book.json" , "w") as f:
                        json.dump(contacts, f, indent=4) 
                    print(f"{dlt} Contact deleted Succesfully.")
                    return

if __name__=="__main__":
    delete_contacts()
