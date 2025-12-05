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
                if self.transac_amount != None:
                    return self.transac_amount
                else:
                    print("⚠️ - Amount cannot be empty.")
            except ValueError:
                print("❌ Invalid input. Please enter the correct data types. Transaction not created.")


        # while True:
        #     try:
        #         self.transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
        #         if self.transac_type not in ['income', 'expense']:
        #             print("Please only enter 'income' or 'expense'")
        #         self.transac_date = input("Enter transaction date: ")
        #         self.transac_description = input("Briefly describe your transaction: ").capitalize()
        #         amount = input("Enter transaction amount: $")
        #         self.transac_amount = float(amount)
        #         break                                               #⬅️ Exit loop if all inputs are valid
        #     except ValueError:
        #         print("❌ Invalid input. Please enter the correct data types. Transaction not created.")
        #     except AttributeError:
        #         print("Attribute error encountered. Please check your inputs.")  


# IMPORTANT:
# Predefined all attributes before the try/except so they always exist.
# This prevents missing-attribute AttributeErrors.
# Your except blocks now work as intended.

# TODO: Current progress:
# If 'income' or 'expense' is not entered, ValueError is NOT raised yet for some reason, 'continue' unreachable.
# - Only 'ValueError' in 'except' block is being raised.
# - Need to refine that part further, look into it further.