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

        self.transac_type = None          #⬅️ Predefine all attributes so they always exist.
        self.transac_date = None
        self.transac_description = None
        self.transac_amount = None

        try:
            self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
            self.transac_date = input("Enter transaction date: ")
            self.transac_description = input("Briefly describe your transaction: ").capitalize()
            self.transac_amount = float(input("Enter transaction amount: $"))
        except ValueError:
            print("❌ Invalid input. Please enter the correct data types.")
        except AttributeError:
            print("Attribute error encountered. Please check your inputs.")  

# IMPORTANT:
# Predefined all attributes before the try/except so they always exist.
# This prevents missing-attribute AttributeErrors.
# Your except blocks now work as intended.