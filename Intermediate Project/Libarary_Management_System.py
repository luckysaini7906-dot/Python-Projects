#-----------------------------------------
# Import Modules
#-----------------------------------------

import json
import os

# Create Library Data File

Library_Data="Library_Data.json"

#--------------------------------------
# Create Function For Load Data
#--------------------------------------
def Load_Data():

    if os.path.exists(Library_Data):
        with open(Library_Data,"r") as File:
            return json.load(File)
    
    return{}

#---------------------------------------
# Create Function For Save Data
#---------------------------------------

def Save_Data(data):

    with open(Library_Data,"w") as File:
        return json.dump(data,File,indent=4)
    
Library_File=Load_Data()

#---------------------------------------
# Create Funciton For Add Book
#---------------------------------------

def Add_Book():

    Book_Id=input("Enter Book Id :")

    if Book_Id in Library_File:

        print("Book Already Exist !")
        return
    
    Title=input("Enter Book Title :")
    Auther=input("Enter Book Auther Name :")

# Create Dectionary

    Library_File[Book_Id] = {
        "Title":Title,
        "Auther":Auther,
        "Status":"Available"
    }

# For Save Updated Data

    Save_Data(Library_File)

    print("Book Added Sucessfully ")

#-------------------------------------------
# Create Function For View Book
#-------------------------------------------

def View_Book():

    Book_Id=input("Enter Book Id :")

    if not Library_File:

        print("Book Not Exist In Library")
        return
    
    print("------Library Book-------")

# Using For Loop

    for Book_Id,details in Library_File.items():

        print("Book Id : ",Book_Id)
        print("Title : ",details["Title"])
        print("Auther : ",details["Auther"])
        print("Status : ",details["Status"])


#------------------------------------------
# Create Function For Search Book
#------------------------------------------

def Search_Book():

    Book_Id=input("Enter Book Id :")

    if Book_Id in Library_File:

        print("-----------------------------------")
        print("======Book Details======")
        print("Book Id : ",Book_Id)
        print("Book Title : ",Library_File[Book_Id]["Title"])
        print("Book Auther : ",Library_File[Book_Id]["Auther"])
        print("Book Status :   ",Library_File[Book_Id]["Status"])

    else:

        print("Book Not Exist In Library")

#----------------------------------------
# Create Function For Borrow Book
#----------------------------------------

def Borrow_Book():

    Book_Id=input("Enter Book Id :")

    if Book_Id not in Library_File:

        print("Book Not Found ")
        return
    
    if Library_File[Book_Id]["Status"]=="Borrowed":
        print("Book Alerady Borrowed")

    else:

        Library_File[Book_Id]["Status"]="Borrowed"

# For Save Updated Data

        Save_Data(Library_File)

        print("Book Borrowed Sucessfully")

#----------------------------------------
# Create Function For Return Book
#----------------------------------------

def Return_Book():

    Book_Id=input("Enter Book Id :")

    if Book_Id not in Library_File:

        print("Book not Found")

    if Library_File[Book_Id]["Status"]=="Available":

        print("Book Already Available")

    else:

        Library_File[Book_Id]["Status"]="Available"

# For Save Updated Data

        Save_Data(Library_File)

        print("Book Returned Sucessfully")

#--------------------------------------------
# Create Function For Delete Book
#--------------------------------------------

def Delete_Book():

    Book_Id=input("Enter Book Id :")

    if Book_Id not in Library_File:

        print("Book not Found")

    else:

        del Library_File[Book_Id]

# For Save Updated Data

        Save_Data(Library_File)

        print("Book Deleted Sucessfully")

# Create While Loop

while True:

    print("Library Management System")

    print("============================")
    print("-----------MENU------------")
    print("============================")

    print("1. Add Book")

    print("2. View Book")

    print("3. Search Book")

    print("4. Borrow Book")

    print("5. Return Book")

    print("6. Delete Book")

    print("7. Exit")

# Take User Input For Perform Tasks

    User_Input=input("Enter Your Choice To Perform Tasks :")

    if User_Input=="1":

        Add_Book()

    elif User_Input=="2":

        View_Book()

    elif User_Input=="3":

        Search_Book()

    elif User_Input=="4":

        Borrow_Book()

    elif User_Input=="5":

        Return_Book()

    elif User_Input=="6":

        Delete_Book()

    elif User_Input=="7":

        print("Thanks For Using Library Management Syatem")
        break

    else:

        print("Invalid Choice ! Please Try Again Later")
        
