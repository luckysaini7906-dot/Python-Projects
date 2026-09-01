tasks=[]

while True:
    print("\n Hello ! Welcome TO DO List View App")
    print("1. Add")
    print("2. View")
    print("3. Remove")
    print("4. Exit")

    choice=input("\n Enter Your Choice (1-4) :")

    if choice=="1":

        add_some=input("\n Enter Your Tasks To Add Here :")
        tasks.append(add_some) 
        print("\n Tasks Added Successfully ") 

    elif choice=="2":

        if len(tasks)==0:
            print("\n Tasks Are Not Available To View !")

        else:

            for i in range(len(tasks)):
                    print(i,".",tasks[i])
        

    elif choice=="3":

        if len(tasks)==0:
            print("\n No Tasks Availabal To Remove !")
            print("\n Please Add Some Tasks First ")

        else:

            remove_some=int(input("\n Enter Your Tasks Number To Remove : "))
            if 0<=remove_some<=len(tasks):
                tasks.remove(tasks[remove_some])
                print("Tasks Remove Successfully")
        
    elif choice=="4":
    
        print("Thank You For Using To Do List App View")
        break

    else:
        print("Invalid Choice ! Please Try Again Later ")
