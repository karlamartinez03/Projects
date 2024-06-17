transactions = []

def display_menu():
    print("\nPersonal Budget Tracker")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. View Transactions")
    print("5. Exit")



def add_transaction(is_income):
    description = input("Enter description: ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("invalid amount. Please enter a number.")
        return 
    category = input("Enter category: ")
    transaction = {
        "description": description,
        "amount": amount if is_income else -amount, 
        "category": category
    }
    transactions.append(transaction)

