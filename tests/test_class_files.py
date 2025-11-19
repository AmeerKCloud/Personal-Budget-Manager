# Here go all of the test-class code.

class Transaction:                                         #⬅️ This class is working as desired.
    def __init__(self, type, date, description, amount):
        self.type = type
        self.date = date
        self.description = description
        self.amount = amount

    def transac_data(self):
        """Stores type (“income” or “expense”), 
        description, and amount."""

        transac_dict = {
            "income" : [],
            "expense" : [],
        }

        for key in transac_dict:
            if self.type == key:
                new_dict = {}
                new_dict["date"] = self.date
                new_dict["description"] = self.description
                new_dict["amount"] = self.amount
                transac_dict[key].append(new_dict)
        return transac_dict


class Budget:                           #⬅️Currently trying to figure out how to make use of this class
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
        """Displays entire history of all transactions"""
        pass

while True:

    transac_type = input("\nEnter your transaction type: 'income' or 'expense'? ").lower()
    transac_date = input("Enter todays date: ")
    transac_description = input("Briefly describe your transaction: ").capitalize()
    transac_amount = float(input("Enter your transaction amount: $"))

    transaction = Transaction(transac_type, transac_date, transac_description, transac_amount)    #⬅️ Object
    transac_data = transaction.transac_data()
    print(transac_data)

    for key in transac_data:
        # if key == "income" or key == "expense":
        for item in range(len(transac_data[key])):
            monetary_amount = transac_data[key][item]["amount"] 
    print(monetary_amount)
    print(type(monetary_amount))

    exit = input("Exit? 'y' or 'n'? ").lower()

    if exit == "y":
        break



#TODO: 
# - Currently trying to figure how to make use of the info from the completed 'Transaction'
# class to input it into the 'Budget' class to make use of that class as per the program 
# requirements.
# - - Previous entry gets erased 
# - - - Might be caused by the object 'transaction' being placed within the 'while' loop?









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









