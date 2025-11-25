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


class Budget:                           #⬅️Currently trying to figure out how to make use of this class
    """Stores total available money.
    Stores all transactions in a list."""

    def __init__(self):
        self.all_transactions = {
            "income": [],
            "expense": [],
        }
        self.total_available_money = 0

    def add_income(self, money):
        """Returns the sum of all income transactions."""
        income_total = 0
        income_total += money
        print(f"Your total income: ${income_total}")

    def add_expense(self, money):
        """Returns the sum of all expense transactions."""
        expense_total = 0
        expense_total += money
        print(f"Your total expenses: ${expense_total}")

    def calculate_balance(self):
        income_total = sum(item["amount"] for item in self.all_transactions["income"]) #⬅️ Extracting amount values from list of dicts & summing them.
        expense_total = sum(item["amount"] for item in self.all_transactions["expense"])
        self.total_available_money = income_total - expense_total
        print(f"Your total available balance is: ${self.total_available_money}")

    def show_transactions(self, transaction, transac_type):
        """Displays entire history of all transactions"""
        self.transac_type = transac_type
        self.transaction = transaction

        self.all_transactions[self.transac_type].append(self.transaction)  #⬅️ Keep reviewing to understand the logic here.
        print(f"\nAll your transactions so far:")
        print(f"Income: {self.all_transactions['income']}")
        print(f"Expense: {self.all_transactions['expense']}")



budget = Budget()   #⬅️ Object

while True:

    user_choice = input("\nChoose an option: (a) Add new transaction, (b) view all transactions, (c) view income total, (d) view expense total, (e) view balance, (f) exit: ").lower()

    if user_choice == "a":

        #⬇️ Perhaps these set of inputs need to go into option 'b' in order for the error messages to stop?
        
        transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
        transac_date = input("Enter transaction date: ")
        transac_description = input("Briefly describe your transaction: ").capitalize()
        transac_amount = float(input("Enter transaction amount: $"))

        transaction = Transaction(transac_type, transac_date, transac_description, transac_amount)    #⬅️ Object
        current_transac_data = transaction.current_transac_data()

        for key in current_transac_data:
            if key == transac_type:
                for list_item in current_transac_data[key]:
                    transaction = list_item                     #⬅️ This is the dict. inside the list.
                    monetary_amount = list_item["amount"]       #⬅️ This is the amount value inside the dict.
            budget.show_transactions(transaction, key)
    elif user_choice == "b":
        current_transac_data = transaction.current_transac_data()
        for key in current_transac_data:                        #⬅️ Getting ERROR: here if user selects 'b' first.
            if key == transac_type:
                for list_item in current_transac_data[key]:
                    transaction = list_item                     
                    monetary_amount = list_item["amount"]       
            budget.show_transactions(transaction, key)
        # budget.show_transactions(transaction, key)
    elif user_choice == "c":
        budget.add_income(monetary_amount)
    elif user_choice == "d":
        budget.add_expense(monetary_amount)
    elif user_choice == "e":
        budget.calculate_balance()
    else:
        break

    exit = input("Exit? 'y' or 'n'? ").lower()

    if exit == "y":
        break



#TODO: Describe the problem:
# - Currently trying to print different outputs based on user choice.




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





# -------------- ⬇️ Reserve Code ⬇️ ----------------



#______ Reserve 3 _______:

# class Transaction:                                         #⬅️ This class is working as desired.
#     def __init__(self, type, date, description, amount):
#         self.type = type
#         self.date = date
#         self.description = description
#         self.amount = amount

#     def current_transac_data(self):
#         """Stores type (“income” or “expense”), 
#         description, and amount."""

#         current_transac_dict = {
#             "income" : [],
#             "expense" : [],
#         }

#         for key in current_transac_dict:
#             if self.type == key:
#                 new_dict = {}
#                 new_dict["type"] = self.type
#                 new_dict["date"] = self.date
#                 new_dict["description"] = self.description
#                 new_dict["amount"] = self.amount
#                 current_transac_dict[key].append(new_dict)
#         return current_transac_dict


# class Budget:                           #⬅️Currently trying to figure out how to make use of this class
#     """Stores total available money.
#     Stores all transactions in a list."""

#     def __init__(self, money, transac_type, transaction):
#         self.money = money
#         self.transac_type = transac_type
#         self.transaction = transaction
#         self.all_transactions = {}
#         self.total_available_money = 0

#     def add_income(self):
#         """Returns the sum of all income transactions."""
#         pass

#     def add_expense(self):
#         """Returns the sum of all expense transactions."""
#         pass

#     def calculate_balance(self):
#         pass

#     def show_transactions(self):
#         """Displays entire history of all transactions"""
        
#         self.all_transactions[self.transac_type] = self.transaction
#         print(self.all_transactions)

# while True:

#     transac_type = input("\nEnter your transaction type: 'income' or 'expense'? ").lower()
#     transac_date = input("Enter todays date: ")
#     transac_description = input("Briefly describe your transaction: ").capitalize()
#     transac_amount = float(input("Enter your transaction amount: $"))

#     transaction = Transaction(transac_type, transac_date, transac_description, transac_amount)    #⬅️ Object
#     current_transac_data = transaction.current_transac_data()
#     print(current_transac_data)

#     for key in current_transac_data:
#         if key == transac_type:
#             for list_item in current_transac_data[key]:
#                 key = key
#                 transaction = current_transac_data[key]
#                 monetary_amount = list_item["amount"]
#             budget = Budget(monetary_amount, key, transaction)   #⬅️ Object
#             budget.show_transactions()
#     # print(monetary_amount)
#     # print(type(monetary_amount))
#     # print(transaction)

#     exit = input("Exit? 'y' or 'n'? ").lower()

#     if exit == "y":
#         break



#______ Reserve 4 _______:

# class Transaction:                                         #⬅️ This class is working as desired.
#     def __init__(self, type, date, description, amount):
#         self.type = type
#         self.date = date
#         self.description = description
#         self.amount = amount

#     def current_transac_data(self):
#         """Stores type (“income” or “expense”), 
#         description, and amount."""

#         current_transac_dict = {
#             "income" : [],
#             "expense" : [],
#         }

#         for key in current_transac_dict:
#             if self.type == key:
#                 new_dict = {}
#                 new_dict["type"] = self.type
#                 new_dict["date"] = self.date
#                 new_dict["description"] = self.description
#                 new_dict["amount"] = self.amount
#                 current_transac_dict[key].append(new_dict)
#         return current_transac_dict


# class Budget:                           #⬅️Currently trying to figure out how to make use of this class
#     """Stores total available money.
#     Stores all transactions in a list."""

#     def __init__(self):
#         self.all_transactions = {
#             "income": [],
#             "expense": [],
#         }
#         self.total_available_money = 0

#     def add_income(self, money):
#         """Returns the sum of all income transactions."""
#         income_total = 0
#         income_total += money
#         print(f"Your total income: ${income_total}")

#     def add_expense(self, money):
#         """Returns the sum of all expense transactions."""
#         expense_total = 0
#         expense_total += money
#         print(f"Your total expenses: ${expense_total}")

#     def calculate_balance(self):
#         income_total = sum(item["amount"] for item in self.all_transactions["income"]) #⬅️ Extracting amount values from list of dicts & summing them.
#         expense_total = sum(item["amount"] for item in self.all_transactions["expense"])
#         self.total_available_money = income_total - expense_total
#         print(f"Your total available balance is: ${self.total_available_money}")

#     def show_transactions(self, transaction, transac_type):
#         """Displays entire history of all transactions"""
#         self.transac_type = transac_type
#         self.transaction = transaction

#         self.all_transactions[self.transac_type].append(self.transaction)  #⬅️ Keep reviewing to understand the logic here.
#         print(self.all_transactions)



# budget = Budget()   #⬅️ Object

# while True:

#     transac_type = input("\nEnter transaction type: 'income' or 'expense'? ").lower()
#     transac_date = input("Enter transaction date: ")
#     transac_description = input("Briefly describe your transaction: ").capitalize()
#     transac_amount = float(input("Enter transaction amount: $"))

#     transaction = Transaction(transac_type, transac_date, transac_description, transac_amount)    #⬅️ Object
#     current_transac_data = transaction.current_transac_data()

#     for key in current_transac_data:
#         if key == transac_type:
#             for list_item in current_transac_data[key]:
#                 key = key
#                 transaction = list_item                     #⬅️ This is the dict. inside the list.
#                 monetary_amount = list_item["amount"]       #⬅️ This is the amount value inside the dict.
#             budget.show_transactions(transaction, key)
#             budget.add_income(monetary_amount)
#             budget.add_expense(monetary_amount)
#             budget.calculate_balance()

#     exit = input("Exit? 'y' or 'n'? ").lower()

#     if exit == "y":
#         break



