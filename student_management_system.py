#-------------------------------------
# Import Module
#-------------------------------------

import json
import os

#----------Create Student File----------

Student_Data="Student_Data.json"

#--------------------------------------
# Define Load Data Function
#--------------------------------------

def load_data():

    if os.path.exists(Student_Data):
        with open(Student_Data,"r") as Data_File:
            return json.load(Data_File)
    return{}

#--------------------------------------
# Define Save Data Function
#--------------------------------------

def save_data(data):

    with open(Student_Data,"w") as Data_File:
        return json.dump(data,Data_File,indent=4)
    
Student_account=load_data()

#--------------------------------------
# Define Add Student Function
#--------------------------------------

def Add_Student():

    Student_Name=input("Enter Student Name :")

    if Student_Name in Student_account:
        print("Student Alerady Exist")
        return
    
    Student_RollNo=int(input("Enter Student Roll :"))
    Student_Grade=input("Enter Student Grade :")
    Student_Age=int(input("Enter Student Age :"))

    Student_account[Student_Name]={
        "Student Roll Number":Student_RollNo,
        "Student Grade":Student_Grade,
        "Student Age":Student_Age
    }

    save_data(Student_account)
    print("Student Added Sucessfully ")

#--------------------------------------
# Define Search Student Function
#--------------------------------------

def Search_Student():

    Student_Name=input("Enter Student Name :")

    if Student_Name not in Student_account:
        print("Student Not Exists In Students Data")

    else:
        print("Student_Name",Student_Name)
        print("Student Roll No",Student_account[Student_Name]["Student Roll Number"])
        print("Student Grade",Student_account[Student_Name]["Student Grade"])
        print("Student Age",Student_account[Student_Name]["Student Age"])

#--------------------------------------
# Define Print All Student Function
#--------------------------------------

def All_Student():

    if not Student_account:
        print("Student Not Exist In Students Data ")

    else:

        for Student_Name,details in Student_account.items():
            print("--------All Students---------")
            print("-----------------------------------------------------")
            print("Student Name :",Student_Name)
            print("Student Roll Number :",details["Student Roll Number"])
            print("Student Grade :",details["Student Grade"])
            print("Student Age",details["Student Age"])

#-------------------------------------
# Define Update Student Function
#-------------------------------------

def Update_Student():

    Student_Name=input("Enter Student name :")

    if Student_Name not in Student_account:
        print("Student Not Exist In Student Data")

    else:

        Update_Rollno=int(input("Enter Student Roll Number"))
        Update_Grade=input("Enter Student Grade :")
        Update_Age=input("Enter Student Age")


        Student_account[Student_Name]={
            "Student Roll Number":Update_Rollno,
            "Student Grade":Update_Grade,
            "Student Age":Update_Age
        }

        save_data(Student_account)
        print("Student Update Sucessfully")

#--------------------------------------
# Define Delete Student Function
#--------------------------------------

def Delete_Student():

    Student_Name=input("Enter Student Name")

    if Student_Name not in Student_account:
        print("Student Not Exist In Student Data")

    else:

        del Student_account[Student_Name]
        print("Student Deleted Sucessfully")

#-----------------------------------------------------
# Define While Loop For Menu And Function Calling
#-----------------------------------------------------

while True:

    print("-----------Menu-----------")
    print("==========Student Management System==========")

    print("1. Add Student")

    print("2. Search Student")

    print("3. Display All Students")

    print("4. Update Student")

    print("5. Delete Student")

    print("6. Exit")

# User Choice for Run Multiple Function 

    User_Input=input("Enter Your Choice :")

    if User_Input=="1":
        Add_Student()

    elif User_Input=="2":
        Search_Student()

    elif User_Input=="3":
        All_Student()

    elif User_Input=="4":
        Update_Student()

    elif User_Input=="5":
        Delete_Student()

    elif User_Input=="6":

        print("Thanks ! For Using Student Msnagement System")
        break
    
    else:
        print("Invalid Choice ,Please Try Again !")



