

class Transaction:
    """Stores type (“income” or “expense”), description, and amount."""
    def __init__(self, type, description, amount):
        self.type = type
        self.description = description
        self.amount = amount            #⬅️ Let this be a integer

    def transac_data(self):
        transac_dict = {} 
        transac_dict[self.type] = {}     #⬅️ Currently here, figuring out how to add user inputs as key-values
        transac_dict[self.type]["description"] = self.description
        transac_dict[self.type]["amount"] = self.amount
        print(transac_dict)


class Budget:
    """Stores total available money.
    Stores all transactions in a list."""

    def __init__(self, money, transaction):
        self.money = money
        all_transactions = []
        total_available_money = 0
        pass

transac_type = input("\nEnter your transaction type: 'income' or 'expense'? ").lower()
transac_description = input("Briefly describe your transaction: ").capitalize()
transac_amount = int(input("Enter your transaction amount: $"))

transaction = Transaction(transac_type, transac_description, transac_amount)
transaction.transac_data()