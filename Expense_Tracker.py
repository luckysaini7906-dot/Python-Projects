#-----------------------------------------------
# Import Modules
#-----------------------------------------------


import json
import os
from datetime import datetime

# Create Json File For Store Data

Expences="Expences_Record.json"

#------------------------------------------------
# Define Load Data Function
#------------------------------------------------


def Load_Data():

    if os.path.exists(Expences):

        with open(Expences,"r") as File:

            return json.load(File)



    return[]  

#------------------------------------------
# Define Save Data Function 
#------------------------------------------


def Save_Data(data):

    with open(Expences,"w") as File:

        return json.dump(data,File,indent=4)


expences=Load_Data()

#-------------------------------------------
# Define Add Expences Function
#-------------------------------------------

def Add_Expences():

    expence = {
        "ID" :len(expences)+1,
        "Date" : input("Enter Date (yyyyy-mm-dd) :"),
        "Category" :input("Enter Category :"),
        "Description" :input("Enter Description :"),
        "Amount": float(input("Enter Amount :"))
    }


    expences.append(expence)
    Save_Data(expences)
    print("Expences Added sucesfully")

#-------------------------------------------
# Define View Expences Function  
#-------------------------------------------
def View_Expence():

    if not expences:

        print("Expences Not Found")

    else:

        print("-------------ALL EXPENCES-------------")

        for exp in expences:

            print("----------------------------------")

            print("ID : ",exp["ID"])
            print("Date : ",exp["Date"])
            print("Category : ",exp["Category"])
            print("Description : ",exp["Description"])
            print("Amount : ",exp["Amount"])


#-------------------------------------------
# Define Search Expenses Function
#-------------------------------------------
def Search_Expences():

    if not expences:

        print("Expences Not Found")

    else:

        User_Input =input("Enter Category To Search :")
        User_Input1=input("Enter Description To Search :")

        for exp in expences:

            if User_Input==exp["Category"]:

                if User_Input1==exp["Description"]:

                    print("ID : ",exp["ID"])
                    print("Date : ",exp["Date"])
                    print("Category : ",exp["Category"])
                    print("Description : ",exp["Description"])
                    print("Amount : ",exp["Amount"])


#---------------------------------------------
# Define Update Expenses Function 
#---------------------------------------------

def Update_Expences():

    ID=int(input("Enter Your ID To Update Expences"))

    found=False

    for exp in expences:

        if exp["ID"]==ID:

            exp["Date"]=input("Enter Date (yyyy-mm-dd) :")
            exp["Category"]=input("Enter Category :")
            exp["Description"]=input("Enter Description :")
            exp["Amount"]=float(input("Enter Amount :"))

            found=True


            Save_Data(expences)

            print("Expences Updated Sucessfully ")

        else:

            print("No Expences Found")

#----------------------------------------------
# Define Delete Expences Function 
#----------------------------------------------

def Delete_Expences():

    ID=int(input("Enter ID For Delete Expences :"))

    found= False

    for exp in expences:

        if exp["ID"]==ID:

            expences.remove(exp)

            found=True

            Save_Data(expences)
            print("Expences Deleted Sucessfully")

        else:
            print("Expences Not Found")

#--------------------------------------------
# Define Monthly Summery Function
#--------------------------------------------

def Monthly_Summery():

    Month=input("Enter Month (yyyy-mm)")
    total=0

    for exp in expences:

        if exp["Date"].startwith(Month):
            total+=exp["Amount"]

    print(f"Total Expences Of {Month} :", total)

#--------------------------------------------
# Define Category Summery Function
#--------------------------------------------


def Category_Summery():

    Summery={}

    for exp in expences:

        category=exp["Category"]

        Summery[category]= Summery.get(category,0) + exp["Amount"]

    print("Category Wise Expences ")
    
    for key,value in Summery.items():
        print(f"{key}:{value}")

#-------------------------------------------
# Define Total Expenses Function
#-------------------------------------------

def Total_Expences():

    total= sum( exp["Amount"] for exp in expences)
    print(f"Total Expences : {total}")

# Create While Loop

while True:

    print("------------------MENU-------------------")
    print("============EXPENSE TRACKER============")

# Create Menu For Perform Multiple Tasks

    print("1. Add Expense")
    print("2. View Expense")
    print("3. Search Expenses")
    print("4. Update Expenses")
    print("5. Delete Expenses")
    print("6. Monthly Summery")
    print("7. Category Summery")
    print("8. Total Expenses")
    print("9. Exit")

# Define Statement For Input User Value  to Perform Tasks


    User_Input=input("Enter Your Choice To Perform Task :")


    if User_Input=="1":
        Add_Expences()

    elif User_Input=="2":
        View_Expence()
    
    elif User_Input=="3":
        Search_Expences()

    elif User_Input=="4":
        Update_Expences()

    elif User_Input=="5":
        Delete_Expences()

    elif User_Input=="6":
        Monthly_Summery()

    elif User_Input=="7":
        Category_Summery()

    elif User_Input=="8":
        Total_Expences()
    
    elif User_Input=="9":


        print("Thanks ! For Using Expanses Tracker")
        break

    else:

        print("Invalid Choice ! Please Try Again Later")
