import json
import os
from datetime import datetime

FILE_NAME = "Expenses.json"


# -----------------------------
# Load Data
# -----------------------------
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# -----------------------------
# Save Data
# -----------------------------
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


expenses = load_data()


# -----------------------------
# Add Expense
# ----------- ------------------
def Add_Expense():

    expense = {
        "ID": len(expenses) + 1,
        "Date": input("Enter Date (YYYY-MM-DD): "),
        "Category": input("Enter Category: "),
        "Description": input("Enter Description: "),
        "Amount": float(input("Enter Amount: "))
    }

    expenses.append(expense)
    save_data(expenses)
    print("\nExpense Added Successfully.")


# -----------------------------
# View Expenses
# -----------------------------
def View_Expenses():

    if not expenses:
        print("\nNo Expenses Found.")
        return

    print("\n------------- Expenses -------------")

    for exp in expenses:

        print(f"""
ID          : {exp['ID']}
Date        : {exp['Date']}
Category    : {exp['Category']}
Description : {exp['Description']}
Amount      : ₹{exp['Amount']}
-----------------------------------------
""")


# -----------------------------
# Search Expense
# -----------------------------
def Search_Expense():

    keyword = input("Enter Category or Description: ").lower()

    found = False

    for exp in expenses:

        if keyword in exp["Category"].lower() or keyword in exp["Description"].lower():

            print(exp)
            found = True

    if not found:
        print("Expense Not Found.")


# -----------------------------
# Update Expense
# -----------------------------
def Update_Expense():

    ID = int(input("Enter Expense ID: "))

    for exp in expenses:

        if exp["ID"] == ID:

            exp["Date"] = input("New Date: ")
            exp["Category"] = input("New Category: ")
            exp["Description"] = input("New Description: ")
            exp["Amount"] = float(input("New Amount: "))

            save_data(expenses)

            print("Expense Updated Successfully.")
            return

    print("Expense Not Found.")


# -----------------------------
# Delete Expense
# -----------------------------
def Delete_Expense():

    ID = int(input("Enter Expense ID: "))

    for exp in expenses:

        if exp["ID"] == ID:

            expenses.remove(exp)
            save_data(expenses)

            print("Expense Deleted Successfully.")
            return

    print("Expense Not Found.")


# -----------------------------
# Monthly Summary
# -----------------------------
def Monthly_Summary():

    month = input("Enter Month (YYYY-MM): ")

    total = 0

    for exp in expenses:

        if exp["Date"].startswith(month):
            total += exp["Amount"]

    print(f"\nTotal Expense of {month} : ₹{total}")


# -----------------------------
# Category Summary
# -----------------------------
def Category_Summary():

    summary = {}

    for exp in expenses:

        category = exp["Category"]

        summary[category] = summary.get(category, 0) + exp["Amount"]

    print("\nCategory Wise Expense\n")

    for key, value in summary.items():

        print(f"{key} : ₹{value}")


# -----------------------------
# Total Expense
# -----------------------------
def Total_Expense():

    total = sum(exp["Amount"] for exp in expenses)

    print(f"\nTotal Expense : ₹{total}")


# -----------------------------
# Menu
# -----------------------------
while True:

    print("""
========== Expense Tracker ==========
1. Add Expense
2. View Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Monthly Summary
7. Category Summary
8. Total Expense
9. Exit
""")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        Add_Expense()

    elif choice == "2":
        View_Expenses()

    elif choice == "3":
        Search_Expense()

    elif choice == "4":
        Update_Expense()

    elif choice == "5":
        Delete_Expense()

    elif choice == "6":
        Monthly_Summary()

    elif choice == "7":
        Category_Summary()

    elif choice == "8":
        Total_Expense()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")