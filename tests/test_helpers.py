# Here will be additional helper classes to the budget program.

class UserInputs:
    """Handles all user inputs for transactions."""
    """Does not handle exceptions yet."""
    def __init__(self):

        #⬇️ Predefine all attributes so they always exist.
        self.transac_type = None
        self.transac_date = None
        self.transac_description = None
        self.transac_amount = None        #⬅️ Still gets added as 'None' if invalid input is given.

        try:
            self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
            self.transac_date = input("Enter transaction date: ")
            self.transac_description = input("Briefly describe your transaction: ").capitalize()
            self.transac_amount = float(input("Enter transaction amount: $"))
        except ValueError:
            print("❌ Invalid input. Please enter the correct data types. Transaction not created.")
        except AttributeError:
            print("Attribute error encountered. Please check your inputs.")  


# IMPORTANT:
# Predefined all attributes before the try/except so they always exist.
# This prevents missing-attribute AttributeErrors.
# Your except blocks now work as intended.