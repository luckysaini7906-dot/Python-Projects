#----------------------------------
# Import Module
#----------------------------------

import json
import os
 
File_Name="Accounts_Data.json"

def load_data():

    if os.path.exists(File_Name):
        with open(File_Name,"r") as file:
            return json.load(file)
    return{}

def save_data(data):

    with open(File_Name,"w") as file:
        return json.dump(data,file,indent=4)
    
accounts=load_data()

#-----------------------------------
#Create Account
#-----------------------------------

def Create_Account():

    account_no=input("Enter Your Account Number :")
    
    if account_no in accounts:
        print("Account Number Already Exist!")
        return
    
    Name=input("Enter Account Holder's Name :")
    Balance=float(input("Enter Initial Deopsit :"))

    accounts[account_no]={
        "Name":Name,
        "Balance":Balance
    }

    save_data(accounts)
    print("Account Created Sucessfully")

#------------------------------------
# Deposit Money
#------------------------------------

def deposit():

    account_no=input("Enter Your Account Number :")

    if account_no not in accounts:
        print("Account Not Found")
        return
    
    amount=float(input("Enter Your Amount :"))
    accounts[account_no]["Balance"]+=amount

    save_data(accounts)

    print("Your Amount Deposit Sucessfully")
    print("Total Balance :",accounts[account_no]["Balance"])

#------------------------------------
# Withdraw Money
#------------------------------------

def withdraw():

    account_no=input("Enter Your Account Number")
    if account_no not in accounts:
        print("Account Not Found")
        return
    
    amount=float(input("Enter Your Amount :"))

    if accounts[account_no]["Balance"]>amount:
        accounts[account_no]["Balance"]-=amount
        save_data(accounts)
        print("Withraw Sucessfully")
        print("Ramaining Amount :",accounts[account_no]["Balance"])

    else:

        print("Insufficent Balance ")

#------------------------------------
# Check Balance
#------------------------------------

def check_balance():

    account_no=input("Enter Your Account number :")

    if account_no in accounts:
        print("Account Number :",account_no)
        print("Name :",accounts[account_no]["Name"])
        print("Balance :",accounts[account_no]["Balance"])
    else:

        print("Account Not Found")

#-----------------------------------
# Display Account
#-----------------------------------

def display_account():

    if not accounts:
        print("Account Not Found ")
        return
    
    print("\n All Accounts ")

    for account_no, details in accounts.items():
        print("--------All Accounts--------")
        print("------------------------------------")
        print("Account Number",account_no)
        print("Name",details["Name"])
        print("Balance",details["Balance"])

#----------------------------------
# Search Account
#----------------------------------
    
def search_account():

    account_no=input("Enter Your Acoount Number :")
    if account_no in accounts:
        print("Account Number :",account_no)
        print("Name ",accounts[account_no]["Name"])
        print("balance",accounts[account_no]["Balance"])

    else:
        print("Account Not Found")
    
#----------------------------------
# Delete Account
#----------------------------------

def delete_account():

    account_no=input("Enter Your Acoount Number")
    if account_no in accounts:
        del accounts[account_no]
        save_data(accounts)
        print("Acoount Deleted Sucessfully")

    else:
        print("Account Not Found")

#-------------------------------
# Menu
#-------------------------------

while True:
    print("---------------Bank Management System---------------")

    print("1.Create Account")

    print("2.Deposit Amount")

    print("3.Withdraw Amount")

    print("4.Check Balance")

    print("5.Display Accounts")

    print("6.Search Account")

    print("7.Delete Account")

    print("8.Exit")

    User_Choice=int(input("Enter Your Choice :"))
    
    if User_Choice==1:
        Create_Account()

    elif User_Choice==2:
        deposit()

    elif User_Choice==3:
        withdraw()

    elif User_Choice==4:
        check_balance()

    elif User_Choice==5:
        display_account()

    elif User_Choice==6:
        search_account()

    elif User_Choice==7:
        delete_account()

    elif User_Choice==8:

        print("Thanks For Using Bank Managment System App")
        break

    else:

        print("Invalid Choice, Please Try Again !")
