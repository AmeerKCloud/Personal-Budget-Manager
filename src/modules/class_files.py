

class Transaction:
    """Stores type (“income” or “expense”), description, and amount."""
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount            #⬅️ Let this be a integer
        self.income = {}
        self.expense = {}


class Budget:
    """Stores total available money.
    Stores all transactions in a list."""

    def __init__(self, money, transaction):
        self.money = money
        all_transactions = []
        total_available_money = 0
        pass


