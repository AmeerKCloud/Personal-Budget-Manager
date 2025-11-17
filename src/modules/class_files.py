

class Transaction:
    def __init__(self, type, date, description, amount):
        self.type = type
        self.date = date
        self.description = description
        self.amount = amount            #⬅️ Let this be a integer

    def transac_data(self):
        """Stores type (“income” or “expense”), 
        description, and amount."""

        transac_dict = {} 
        transac_dict[self.type] = {}
        transac_dict[self.type]["date"] = self.date
        transac_dict[self.type]["description"] = self.description
        transac_dict[self.type]["amount"] = self.amount
        # print(transac_dict)
        return transac_dict


class Budget:
    """Stores total available money.
    Stores all transactions in a list."""

    def __init__(self, money, transaction):
        self.money = money
        all_transactions = []
        total_available_money = 0
        pass

    def add_income(self):
        """Returns the sum of all income transactions."""
        pass

    def add_expense(self):
        """Returns the sum of all expense transactions."""
        pass

    def calculate_balance(self):
        pass

    def show_transactions(self):
        
        pass

transac_type = input("\nEnter your transaction type: 'income' or 'expense'? ").lower()
transac_date = input("Enter todays date: ")
transac_description = input("Briefly describe your transaction: ").capitalize()
transac_amount = int(input("Enter your transaction amount: $"))

transaction = Transaction(transac_type, transac_date, transac_description, transac_amount)
transac_dictionary = transaction.transac_data()

for key, value in transac_dictionary.items():
    print(f"{key}: {value}")
