import json


try:
    with open("contacts_book.json") as c:
        contacts = json.load(c)
except (FileNotFoundError, json.JSONDecodeError):
        contacts = {} 

def Add_contacts():
    name = input("Enter Contact Name:").strip()
    while name=="" or not name.replace(" ","").isalpha():
        print("Name can't be empty and name should consits of alphabets only.")
        name = input("Enter Contact Name:").strip()
    
    if name in contacts:
        print(f"{name} contact already exists, you can update it from update option in menu.")
        return
    
    while True:
        num = input(f"Enter Number for contact {name}:").strip()
        if num.isdigit() and len(num)==11:
            break
        else:
            print(f"Please Enter Number again, entered number is not in digits either not contains 11 number.")
        
    contacts.update({f"{name}" : num})
    with open("contacts_book.json", "w") as f:
        json.dump(contacts, f, indent=4)


    print("New Contact Succesfully Added.")

    
    
        


    
if __name__=="__main__":
    Add_contacts()