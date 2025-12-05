# This is the main file for the program.

from modules.other_helpers import UserInputs
from modules.class_files import Transaction, Budget

budget = Budget()   #⬅️ Object

while True:
    print("\n----- Budget Tracker -----")
    print("|")
    user_choice = input("Choose an option: \n(a) Add new transaction, \n(b) view all transactions, \n(c) view income total, \n(d) view expense total, \n(e) view balance, \n(f) exit:\n ").lower()

    if user_choice == "a":
        user_input = UserInputs()   #⬅️ Object to gather user inputs for transaction details.
        transaction = Transaction(user_input.transac_input(), user_input.date_input(), user_input.description_input(), user_input.amount_input())    #⬅️ Object
        current_transac_data = transaction.current_transac_data()

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
    else:
        break


