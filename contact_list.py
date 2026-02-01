import os
contact = {}

def info(empty_dict):
    os.system("clear")
    while True:
        try:
            cNumber = int(input("Enter Contact Number : "))
            break
        except:
            print("Enter Number!")

    cName = input("Enter Contact Name : ").strip()
    cAddress = input("Enter Contact Address(optional) : ").strip()

    while True:
        cEmail = input("Enter Contact Email(optional) : ").strip()
        if cEmail != "":
            if not cEmail.endswith("@gm"):
                print("Invalid Email!")
                continue

            elif cEmail.endswith("@gm"):
                break

        elif cEmail == "":
            break

    print("Contact Saved!".upper())
    contact.setdefault(cNumber, [cName, cAddress, cEmail])


def add_upd():
    user = input("Enter To Do Following (A)dd (S)how (U)pdate : ").upper()

    if user == 'A':
        while True:
            print("-----------------------------------------------")
            user = input("Enter To Add Contacts (y/n) : ")
            if user == 'y':
                info(contact)
            else:
                break

    elif user == 'S':
        for i in contact.items():
            print(i)
    else:
        pass

# even after pressing else letter not breaking
while True:
    add_upd()

