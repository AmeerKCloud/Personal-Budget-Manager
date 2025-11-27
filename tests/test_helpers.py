# Here will be additional helper classes to the budget program.

from test_class_files import Transaction

class UserInputs:
    """Handles all user inputs for transactions."""
    def __init__(self):
        self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
        self.transac_date = input("Enter transaction date: ")
        self.transac_description = input("Briefly describe your transaction: ").capitalize()
        self.transac_amount = float(input("Enter transaction amount: $"))
    

user_input = UserInputs()

transaction = Transaction(user_input.transac_type, user_input.transac_date, user_input.transac_description, user_input.transac_amount)