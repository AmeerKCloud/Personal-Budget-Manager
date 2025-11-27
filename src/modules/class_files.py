# Here go all of the test-class code.

class Transaction:                                         #⬅️ This class is working as desired.
    def __init__(self, type, date, description, amount):
        self.type = type
        self.date = date
        self.description = description
        self.amount = amount

    def current_transac_data(self):
        """Stores type (“income” or “expense”), 
        description, and amount."""

        self.current_transac_dict = {
            "income" : [],
            "expense" : [],
        }

        for key in self.current_transac_dict:
            if self.type == key:
                new_dict = {}
                new_dict["type"] = self.type
                new_dict["date"] = self.date
                new_dict["description"] = self.description
                new_dict["amount"] = self.amount
                self.current_transac_dict[key].append(new_dict)
        return self.current_transac_dict


class Budget:
    """Stores total available money.
    Stores all transactions in a list."""

    def __init__(self):
        self.all_transactions = {
            "income": [],
            "expense": [],
        }
        self.total_available_money = 0

    def add_transactions(self, transaction, transac_type):
        """Displays entire history of all transactions"""
        self.transac_type = transac_type
        self.transaction = transaction

        self.all_transactions[self.transac_type].append(self.transaction) 

    def add_income(self):
        """Returns the sum of all income transactions."""
        income_total = 0                                                                        #⬅️ My way (more bgnner lvl), bgins here
        for item in self.all_transactions["income"]:
            income_total += item["amount"]
        print(f"Your total income: ${income_total}")                                            #⬅️ Nds here

    def add_expense(self):
        """Returns the sum of all expense transactions."""
        expense_total = sum(item.get("amount", 0) for item in self.all_transactions["expense"]) #⬅️ Copilots way (more efficient)
        print(f"Your total expenses: ${expense_total}")

    def calculate_balance(self):
        income_total = sum(item["amount"] for item in self.all_transactions["income"]) #⬅️ Extracting amount values from list of dicts & summing them.
        expense_total = sum(item["amount"] for item in self.all_transactions["expense"])
        self.total_available_money = income_total - expense_total
        print(f"Your total available balance is: ${self.total_available_money}")

    def show_transactions(self):
        """Displays entire history of all transactions"""

        if self.all_transactions["income"] == [] and self.all_transactions["expense"] == []:
            print("\nNo transactions recorded yet.")
            return
        else:
            print(f"\nAll your transactions so far:")
            print("\n>>> 💲 Income Transactions:")
            for list_item in self.all_transactions["income"]:
                print("---")
                for key, value in list_item.items():
                    print(f"{key.capitalize()}: {value}")
            print("\n>>> 💸 Expense Transactions:")
            for list_item in self.all_transactions["expense"]:
                print("---")
                for key, value in list_item.items():
                    print(f"{key.capitalize()}: {value}")


