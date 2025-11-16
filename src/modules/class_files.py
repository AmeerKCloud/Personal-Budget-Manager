

class Transaction:
    """Stores type (“income” or “expense”), description, and amount."""
    def __init__(self, type, description, amount):
        self.description = description
        self.amount = amount            #⬅️ Let this be a integer
        self.type = type

    def transac_data(self):
        pass


class Budget:
    """Stores total available money.
    Stores all transactions in a list."""

    def __init__(self, money, transaction):
        self.money = money
        all_transactions = []
        total_available_money = 0
        pass



