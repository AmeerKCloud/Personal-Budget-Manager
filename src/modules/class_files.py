

class Transaction:
    """Stores type (“income” or “expense”), description, and amount."""
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        self.income = {}
        self.expense = {}


class Budget:
    """Stores total available money.
    Stores all transactions in a list."""


