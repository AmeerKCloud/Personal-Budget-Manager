from test_class_files import Transaction, Budget

budget = Budget()   #⬅️ Object

while True:
    print("\n")
    print("\n----- Budget Tracker -----")
    print("|")
    user_choice = input("Choose an option: \n(a) Add new transaction, \n(b) view all transactions, \n(c) view income total, \n(d) view expense total, \n(e) view balance, \n(f) exit:\n ").lower()

    if user_choice == "a":
        
        transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
        transac_date = input("Enter transaction date: ")
        transac_description = input("Briefly describe your transaction: ").capitalize()
        transac_amount = float(input("Enter transaction amount: $"))

        transaction = Transaction(transac_type, transac_date, transac_description, transac_amount)    #⬅️ Object
        current_transac_data = transaction.current_transac_data()

        for key in current_transac_data:
            if key == transac_type:
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

#TODO: Describe the CURRENT problem you're working on:


#TODO: What objectives are left to complete?
# Handle errors
# - Invalid amounts
# - Negative numbers
# - Wrong input types
# Transfer finalized code from test files to main folders/files


