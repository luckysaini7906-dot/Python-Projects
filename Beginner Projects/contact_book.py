#---------------------------------------------
# Import Modules
#---------------------------------------------

import json
import os

#Create Contact Book File For Store Contact Data

Contact_Book="Contact_Data.json"

#-----------------------------------------
# Define Load Data Function
#-----------------------------------------

def Load_Data():

    if os.path.exists(Contact_Book):
        with open(Contact_Book,"r") as Data:
            return json.load(Data)
        
    return{}

#------------------------------------------
# Define Save Data Function
#------------------------------------------

def Save_Data(data):

    with open(Contact_Book,"w") as Data:
        return json.dump(data,Data,indent=4)
    
Contact_Data=Load_Data()

#-----------------------------------------------
# Define Add Contact Function For Add Contacts
#-----------------------------------------------

def Add_Contact():

    Contact_Name=input("Enter Contact Name :")
    
    if Contact_Name in Contact_Data:
        print("Contact Name Alerady Exist")
    Contact_number=int(input("Enter Contact Number :"))

    Contact_Data[Contact_Name]={
        "Contact Number":Contact_number
    }

    Save_Data(Contact_Data)
    
#-----------------------------------------------------
# Define Search Contact Function For Search Contact
#-----------------------------------------------------

def serach_contact():

    Contact_Name=input("Enter Contact Name :")

    if Contact_Name in Contact_Data:

        print("Contact_Name : ",Contact_Name)
        print("Contact_Number : ",Contact_Data[Contact_Name]["Contact Number"])

    else:
        
        print("Contact Not Exiest In Contact Data")

#-----------------------------------------------
# Define All Contact Function for View Contact
#-----------------------------------------------

def All_Contact():

    if not Contact_Data:

        print("No Contact Available To View")

    else:

        for Contact_Name,details in Contact_Data.items():
            print("-------------------------------------------------")
            print("Contact_Name : ",Contact_Name)
            print("Contact_Number : ",Contact_Data[Contact_Name]["Contact Number"])
            
#----------------------------------------------------
# Define Update Contact Function For Update Contact
#----------------------------------------------------

def Update_Contact():

    Contact_Name=input("Enter Your Contact Name : ")

    if Contact_Name not in Contact_Data:

        print("Contact Not Available For Update")

    else:

        Update_Number=int(input("Enter Your Update Number :"))
        Contact_Data[Contact_Name]={
            "Contact Number":Update_Number
        }

        Save_Data(Contact_Data)
        
#--------------------------------------------
# Define Delete Contact Function For Delete
#--------------------------------------------

def Delete_Contact():

    Contact_Name=input("Enter Your Contact Name :")

    if Contact_Name in Contact_Data:

        del Contact_Data[Contact_Name]
        print("Contact Dleleted Sucessfully")
        
        Save_Data(Contact_Data)

    else:

        print("No Contact Available To Delete")

#------------------------------------------
# Define while loop
#------------------------------------------

while True:

    print("---------Contact Book Menu---------")

    print("1. Add Contact")

    print("2. Serach Contact")

    print("3. All Contact")

    print("4. Update Contact")

    print("5. Delete Contact")

    print("6. Exit")

#-------------------------------------------------
# Take User Input For Perform Tasks 
#-------------------------------------------------

    User_Input=input("Enter Your Choice to Perform Task : ")

    if User_Input=="1":
        Add_Contact()

    elif User_Input=="2":
        serach_contact()

    elif User_Input=="3":
        All_Contact()

    elif User_Input=="4":
        Update_Contact()

    elif User_Input=="5":
        Delete_Contact()

    elif User_Input=="6":

        print("Thanks To using Contact Book Managemnet App ")
        break

    else:

        print("Invalid Choice ! Please Try Again Later")