import json




def search_contact():
    try:
        with open("contacts_book.json") as f:
            contacts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("There are no contacts saved.")
        exit()
    
    while True:
        search = input("Enter the Contact You want to Serach:")
        if search.replace(" ", "").isalpha():
            if contacts.get(f"{search}") !=None:
                print(f"The contact of {search} is",contacts.get(f"{search}"))
                break
            else:
                print(f"{search} contact isn't saved.")
                break
        else:
            print(f"Enter Valid Contact to search.")
        
if __name__=="__main__":
    search_contact()


