

class Transaction:
    """Stores type (“income” or “expense”), description, and amount."""
    def __init__(self, type, description, amount):
        self.type = type
        self.description = description
        self.amount = amount            #⬅️ Let this be a integer

    def transac_data(self):
        transac_dict = {}
        transac_dict[self.type] = [self.description, self.amount]
        print(transac_dict)


class Budget:
    """Stores total available money.
    Stores all transactions in a list."""

    def __init__(self, money, transaction):
        self.money = money
        all_transactions = []
        total_available_money = 0
        pass

transac_type = input("Enter your transaction type: 'income' or 'expense'? ").lower()

transaction = transaction(transac_type, transac_description, transac_amount)