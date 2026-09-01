#------------------------------------------
# Import Modules
#------------------------------------------

import json
import os

# Create File 

Information="Accounts_details.json"

#-----------------------------------------
# Define Load Data Function
#-----------------------------------------

def Load_Data():

    if os.path.exists(Information):
        
        with open(Information,"r") as File:
            return json.load(File)

    return{
        "Name":"lucky",
        "Account Number":"1234567890",
        "Balance":50000,
        "Pin":2468
    }

#-----------------------------------------
# Define Save Data Function
#-----------------------------------------

def Save_Data(data):

    with open(Information,"w") as File:
        return json.dump(data,File,indent=4)

Account_Info=Load_Data()

#----------------------------------------
#Define Change Pin Function
#----------------------------------------

def Change_Pin():

    Attempt=3

    while Attempt>0:
        
        User_Input=int(input("Enter Your Current Pin :"))

        if User_Input ==Account_Info["Pin"]:

            Update_Pin=int(input("Enter Your Pin To Chnage :"))
            Account_Info["Pin"] = Update_Pin

            Save_Data(Account_Info)

            print("Your Pin Has Changed")
            break
        
        else:

            print("Wronge Pin !")

            Attempt-=1

            print(f"You Have Only {Attempt} Attempt")

    
            

            

    

#---------------------------------------
# Define Check Balance Function
#---------------------------------------

def Check_balance():

    Attempt=3

    while Attempt>0:


        User_Input=int(input("Enter Your Pin :"))

        if User_Input==Account_Info["Pin"]:
            print("Balance :",Account_Info["Balance"])
            break

        else:

            print("Wrong Pin ! Please Try Again")
            Attempt-=1
            print(f"You Have Only {Attempt} Attempt")


#--------------------------------------
# Define Withdraw Money Function
#--------------------------------------

def Withdraw_Money():

    Attempt=3

    while Attempt>0:

        User_Input=int(input("Enter Your Pin :"))

        if User_Input == Account_Info["Pin"]:

            User_Money=int(input("Enter Your Money For Withdraw :"))
            if User_Money>0:

                if User_Money < Account_Info["Balance"]:

                    Account_Info["Balance"] -= User_Money
                    Save_Data(Account_Info)
                    print("Money Withdrawal Sucessfully")
                    break

                else:

                    print("Insufficent Balance ! Please Enter Valid Balance")

            else:

                print("Accept Only Positive Value ,Please Enter Positive Value")
                break
        else:

            print("Wrong Pin ! Please Try Again")
            Attempt-=1
            print(f"You Have Only {Attempt} Attempt")


#------------------------------------------
# Define Deposit Money Function
#------------------------------------------

def Deposit_Money():

    Attempt=3

    while Attempt>0:

        User_Input=int(input("Enter Yout Pin :"))

        if User_Input==Account_Info["Pin"]:

            User_Money=int(input("Enter Your Money For Deposit :"))
            
            if User_Money>0:

                Account_Info["Balance"]+=User_Money
                Save_Data(Account_Info)
                print("Money Deopsit sucessfully")
                break

            else:

                print("Accept Only Positive Value, Please Enter Positive Value")
                break
        else:

            print("Wrong Pin ! Please Try Again")
            Attempt-=1
            print(f"You Have Only {Attempt} Attempt")

#-----------------------------------------
# Define Account Details Function
#-----------------------------------------

def Account_Details():

    Attempt=3

    while Attempt>0:

        User_Input=int(input("Enter Your Pin :"))

        if User_Input==Account_Info["Pin"]:

            print("Name",Account_Info["Name"])
            print("Account Number",Account_Info["Account Number"])
            print("Balance",Account_Info["Balance"])
            print("Pin",Account_Info["Pin"])
            break

        else:

            print("Wrong Pin ! Please Try Again")
            Attempt-=1
            print(f"You Have Only {Attempt} Attempt")

# Create While Loop

while True:

    print("-------- ATM Management System --------")
    print("==========================================")
    print("1. Change Pin")

    print("2. Check Balance")

    print("3. Withdraw Money")

    print("4. Deposit Money")

    print("5. Account Details")

    print("6. Exit")

 # Input User Choice Statement 

    User_Choice=input("Enter Your Choice To Perform Tasks :")

    if User_Choice=="1":
        Change_Pin()

    elif User_Choice=="2":
        Check_balance()

    elif User_Choice=="3":
        Withdraw_Money()

    elif User_Choice=="4":
        Deposit_Money()

    elif User_Choice=="5":
        Account_Details()

    elif User_Choice=="6":

        print("Thanks !, For Using ATM System App")
        break

    else:

        print("Invalid Choice! , Please Try Again Later")
