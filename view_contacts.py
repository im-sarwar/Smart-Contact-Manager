import json
 


def view_contacts(): 
    i = 1
    try:
        with open("contacts_book.json") as f:
            contacts = json.load(f)
            print(f"{"Contact":20} {"Number":<11}")
            print("-"*35)
            for name, num  in contacts.items():
                print(f"{i:4} {name :20} {num:<11}")
                i+=1
    except(FileNotFoundError , json.JSONDecodeError):
        print(f"There are not contacts saved.")
        
    
    
if __name__=="__main__":
    view_contacts()