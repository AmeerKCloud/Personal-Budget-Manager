# Purpose of the 'other_helpers.py' file:
# This module contains helper classes and functions that assist
# with user input handling for the budget program.
# These helpers can be imported and utilized in the main program
# to streamline user interactions and data collection & to improve code organization
# as well as further modularity.

class UserInputs:
    """Handles all user inputs for transactions."""
    """Does not handle exceptions yet."""
    def __init__(self):

        #⬇️ Predefine all attributes so they always exist.
        self.transac_type = None
        self.transac_date = None
        self.transac_description = None
        self.transac_amount = None        #⬅️ Still gets added as 'None' if invalid input is given.

    def transac_input(self):
        while True:
            self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
            if self.transac_type in ['income', 'expense']:
                return self.transac_type
            elif self.transac_type == "":
                print("⚠️ - Type cannot be empty.")
            else:
                print("❌ Invalid entry. Please only enter 'income' or 'expense'")

    def date_input(self):
        while True:
            self.transac_date = input("Enter transaction date (e.g. 11/17/2025): ")
            if self.transac_date.strip() != "":
                return self.transac_date
            else:
                print("⚠️ - Date cannot be empty.")

    def description_input(self):
        while True:
            self.transac_description = input("Briefly describe your transaction: ").capitalize()
            if self.transac_description != "":
                return self.transac_description
            else:
                print("⚠️ - Description cannot be empty.")

    def amount_input(self):
        while True:
            try:
                self.transac_amount = float(input("Enter transaction amount: $"))
                if self.transac_amount <= 0:
                    print("⚠️ - Only enter a positive amount greater than 0.")
                elif self.transac_amount != None:
                    return self.transac_amount
            except ValueError:
                print("❌ ValueError raised. Please enter the correct data types. Transaction not created.") 

# IMPORTANT:
# Predefined all attributes before the try/except so they always exist.
# This prevents missing-attribute AttributeErrors.
# Your except blocks now work as intended.