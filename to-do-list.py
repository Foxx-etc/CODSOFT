import os
os.system("clear")


print("TO DO LIST!")

to_do=[]
completed=[]


while True:
    print("\n-----------------------------\n")
    print("(A)dd (R)emove (S)how (Q)uit (C)ompleted")
    user = input("Enter The Letter To : ").upper()
    print("\n-----------------------------")



    if user == 'A':
        task = input("Enter The Task To Add : ")
        print("TASK ADDED!")
        to_do.append(task)



    elif user == 'S':
        print("PENDINGs...")
        if len(to_do) == 0:
            print("Empty!")
        else:
            for i, j in zip(range(len(to_do)), to_do):
                print(i , j)
        print("\n")
        print("COMPLETED...")
        if len(completed) == 0:
            print("Empty!")
        else:
            for i, j in zip(range(len(completed)), completed):
                print(i , j)




    elif user == 'R':
        print("will only remove from tasks that are pendings".upper())
        while True:
            try:
                no = int(input("Enter The Number Of The Task : "))
                to_do.__delitem__(no)
                break
            except:
                print("Invalid Input! Try Again...")
                break


    elif user == 'C':
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



    elif user == 'Q':
        break



    else:
        print(print("(A)dd (R)emove (S)how (Q)uit"))


    


