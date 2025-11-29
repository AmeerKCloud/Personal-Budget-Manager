# This is the main test file for the budget tracker program.
# Purpose of the 'test_helpers.py' file:
# This module contains helper classes and functions that assist
# with user input handling for the budget program.
# These helpers can be imported and utilized in the main program
# to streamline user interactions and data collection & to improve code organization
# as well as further modularity.

from test_helpers import UserInputs
from test_class_files import Transaction, Budget

budget = Budget()   #⬅️ Object

while True:
    print("\n----- Budget Tracker -----")
    print("|")
    user_choice = input("Choose an option: \n(a) Add new transaction, \n(b) view all transactions, \n(c) view income total, \n(d) view expense total, \n(e) view balance, \n(f) exit:\n ").lower()

    if user_choice == "a":
        user_input = UserInputs()   #⬅️ Object to gather user inputs for transaction details.
        transaction = Transaction(user_input.transac_type, user_input.transac_date, user_input.transac_description, user_input.transac_amount)    #⬅️ Object
        current_transac_data = transaction.current_transac_data()

        if transaction.amount is None:
            print("Transaction amount cannot be None.")
            break

        for key in current_transac_data:
            if key == user_input.transac_type:
                for list_item in current_transac_data[key]:
                    transaction = list_item                     #⬅️ This is the dict. inside the list.
                budget.add_transactions(transaction, key)
    elif user_choice == "b":    
        budget.show_transactions()
    elif user_choice == "c":
        budget.add_income()
    elif user_choice == "d":
        budget.add_expense()
    elif user_choice == "e":
        budget.calculate_balance()
    elif user_choice == "f":
        break
    else:
        print("Invalid option. Try again.")
        break

#TODO: Describe the CURRENT problem you're working on:
# - Transactions with 'None' values can still be created if invalid inputs are given.
# - Need to prevent that from happening.


#TODO: What objectives are left to complete?
# Handle errors:                                 ⚠️ currently working on it.
# - Invalid transaction types
# - Invalid amounts
# - Negative numbers
# - Wrong input types
# - Empty inputs
# - - NOTE: Some of these are partially handled in the UserInputs class.
# - - - But need to refine and improve the exception handling further.
# - - - Currently, transactions with 'None' values can still be created if invalid inputs are given.
# - - - Need to prevent that from happening.
# Transfer finalized code from test files to main folders/files

# Optional TODO: COMPLETED ✅
# Further modularize the code more than you already have by:
# - Making separate class for user inputs
# - - Perhaps this will also include the error/exception-handling functionalities? ⚠️ Working on it.



# _______ Reserve Code _______

# from modules.other_helpers import UserInputs
# from modules.class_files import Transaction, Budget

# budget = Budget()   #⬅️ Object

# while True:
#     print("\n")
#     print("\n----- Budget Tracker -----")
#     print("|")
#     user_choice = input("Choose an option: \n(a) Add new transaction, \n(b) view all transactions, \n(c) view income total, \n(d) view expense total, \n(e) view balance, \n(f) exit:\n ").lower()

#     if user_choice == "a":
        
#         transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
#         transac_date = input("Enter transaction date: ")
#         transac_description = input("Briefly describe your transaction: ").capitalize()
#         transac_amount = float(input("Enter transaction amount: $"))

#         transaction = Transaction(transac_type, transac_date, transac_description, transac_amount)    #⬅️ Object
#         current_transac_data = transaction.current_transac_data()

#         for key in current_transac_data:
#             if key == transac_type:
#                 for list_item in current_transac_data[key]:
#                     transaction = list_item                     #⬅️ This is the dict. inside the list.
#                 budget.add_transactions(transaction, key)
#     elif user_choice == "b":    
#         budget.show_transactions()
#     elif user_choice == "c":
#         budget.add_income()
#     elif user_choice == "d":
#         budget.add_expense()
#     elif user_choice == "e":
#         budget.calculate_balance()
#     else:
#         break