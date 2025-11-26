# Here will be additional classes that will be generic and 
# won't specifically be related to the budget program

from test_class_files import Transaction

class UserInputs:
    def __init__(self):
        self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
        self.transac_date = input("Enter transaction date: ")
        self.transac_description = input("Briefly describe your transaction: ").capitalize()
        self.transac_amount = float(input("Enter transaction amount: $"))