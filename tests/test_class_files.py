# Here go all of the test-class code.

class Transaction:
    def __init__(self, type, date, description, amount):
        self.type = type
        self.date = date
        self.description = description
        self.amount = amount            #⬅️ Let this be a integer

    def transac_data(self):
        """Stores type (“income” or “expense”), 
        description, and amount."""

        transac_list = [] 
        transac_list[self.type] = {}
        transac_list[self.type]["date"] = self.date
        transac_list[self.type]["description"] = self.description
        transac_list[self.type]["amount"] = self.amount
        # print(transac_list)
        return transac_list


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








# #⬇️ Test dictionary

# transac_list = {
#     "income": [
#         {
#             "date": "11/17/2025",
#             "description": "paycheck",
#             "amount": 250,
#         },
#         {
#             "date": "09/10/2025",
#             "description": "groceries",
#             "amount": 100,
#         }
#     ],
#     "expense": [
#         {
#             "date": "10/20/2025",
#             "description": "groceries",
#             "amount": 100,
#         },
#         {
#             "date": "08/15/2025",
#             "description": "groceries",
#             "amount": 100,
#         }
#     ]
# }

# transac_type = input("\nEnter your transaction type: 'income' or 'expense'? ").lower()
# transac_date = input("Enter todays date: ")
# transac_description = input("Briefly describe your transaction: ").capitalize()
# transac_amount = int(input("Enter your transaction amount: $"))

# #⬇️ This for loop adds all user input into new dict. and appends that dict to the list
# for key in transac_list:
#     if transac_type == key:
#         new_dict = {}
#         new_dict["date"] = transac_date
#         new_dict["description"] = transac_description
#         new_dict["amount"] = transac_amount
#         transac_list[key].append(new_dict)
#         print(transac_list[key])









