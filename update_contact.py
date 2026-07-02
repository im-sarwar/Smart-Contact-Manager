import json

def update_contact():

    try:
        with open("contacts_book.json") as f:
            contacts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("There are no Contacts Saved.")
        exit()
    
    while True:
        update = input("---------------"
        "\nEnter the Contact you want to update:")
        if contacts.get(update)!=None:
            num = input(f"Enter the new number for contact {update}:")
            if len(num.strip())==11 and num.strip().isdigit():
                contacts[update] = num
                print(f"{update} contact updated to new number {num}.")
                with open("contacts_book.json" , "w") as f:
                    json.dump(contacts ,f ,indent=4)
                break
            else:
                print("Not Valid Nmuber Entered.")
        else:
            print(f"{update} contacts doesn't exist.")

if __name__=="__main__":
    update_contact()


