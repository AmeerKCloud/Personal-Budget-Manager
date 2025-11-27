# Purpose of the 'other_helpers.py' file:
# This module contains helper classes and functions that assist
# with user input handling for the budget program.
# These helpers can be imported and utilized in the main program
# to streamline user interactions and data collection & to improve code organization
# as well as further modularity.

class UserInputs:
    """Handles all user inputs for transactions."""
    def __init__(self):
        self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
        self.transac_date = input("Enter transaction date: ")
        self.transac_description = input("Briefly describe your transaction: ").capitalize()
        self.transac_amount = float(input("Enter transaction amount: $"))

    