# Here will be additional helper classes to the budget program.

class UserInputs:
    """Handles all user inputs for transactions."""
    def __init__(self):
        self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
        self.transac_date = input("Enter transaction date: ")
        self.transac_description = input("Briefly describe your transaction: ").capitalize()
        self.transac_amount = float(input("Enter transaction amount: $"))
