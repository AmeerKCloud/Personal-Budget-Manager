# Here go all of the test-class code.

transac_dictionary = {
    "income": [
        {
            "date": "11/17/2025",
            "description": "paycheck",
            "amount": 250,
        },
        {
            "date": "09/10/2025",
            "description": "groceries",
            "amount": 100,
        }
    ],
    "expense": [
        {
            "date": "10/20/2025",
            "description": "groceries",
            "amount": 100,
        },
        {
            "date": "08/15/2025",
            "description": "groceries",
            "amount": 100,
        }
    ]
}

transac_type = input("\nEnter your transaction type: 'income' or 'expense'? ").lower()
transac_date = input("Enter todays date: ")
transac_description = input("Briefly describe your transaction: ").capitalize()
transac_amount = int(input("Enter your transaction amount: $"))


for key in transac_dictionary:
    if transac_type == key:
        new_dict = {}
        new_dict["date"] = transac_date
        new_dict["description"] = transac_description
        new_dict["amount"] = transac_amount
        transac_dictionary[key].append(new_dict)
        print(transac_dictionary[key])









