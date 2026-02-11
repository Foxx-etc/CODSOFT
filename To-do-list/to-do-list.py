import os

os.system("clear")
print("TO DO LIST!")

to_do=[]
completed=[]

# the function will be used 3 times in elif condition : 'S' 'R' 'C'
def show(pending, comp):
    print("P E N D I N G...")
    if len(pending) == 0:
        print("Empty!")
    else:
        for i, j in zip(range(len(pending)), pending):
            print(i ,'|', j)
    print("\n")
    print("C O M P L E T E D...")
    if len(comp) == 0:
        print("Empty!")
    else:
        for i, j in zip(range(len(comp)), comp):
            print(i ,'|', j)


while True:
    print("\n-----------------------------\n")
    print("(A)dd (R)emove (S)how (C)ompleted (Q)uit")
    user = input("Enter The Letter To : ").upper()
    print("\n-----------------------------")
    os.system("clear")


    if user == 'A':
        task = input("Enter The Task To Add : ")
        print("TASK ADDED!")
        to_do.append(task)


    elif user == 'S':
        show(to_do, completed)


    elif user == 'R':
        show(to_do, completed)
        print("\n-----------------------------")
        print("will remove only tasks that are pending".upper())
        while True:
            try:
                no = int(input("Enter The Number Of The Task : "))
                to_do.__delitem__(no)
                break
            except:
                print("Invalid Input! Try Again...")
                break
        os.system("clear")

    
    elif user == 'C':
        show(to_do, completed)
        print("\n-----------------------------")
        while True:
            try:
                c = int(input("Enter The No. Of The Task You Completed : "))
                completed.append(to_do[c])
                to_do.__delitem__(c)
                print("Congrats!")
                break
            except:
                print("Invalid Input! Try Again...")
                break
        os.system("clear")

    
    elif user == 'Q':
        break

    else:
        print("Wrong Input, Try Again")
