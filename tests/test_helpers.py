# Here will be additional helper classes to the budget program.

class UserInputs:
    """Handles all user inputs for transactions."""
    """Does not handle exceptions yet."""   #⬅️ Still needs to be done.
    def __init__(self):
        try:
            self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
            self.transac_date = input("Enter transaction date: ")
            self.transac_description = input("Briefly describe your transaction: ").capitalize()
            self.transac_amount = float(input("Enter transaction amount: $"))
        except ValueError:
            print("Invalid input. Please enter the correct data types.")
            # Further exception handling can be implemented here.
