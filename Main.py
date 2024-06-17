transactions = []


##This project accomplishes the goal of creating a personal finance tracker. 
#It creates an empty record of transactions and poblates it. 
# 


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


def view_summary():
    total_income = sum(t["amount"]for t in transactions 
    if t["amount"]>0)
    total_expenses = sum(t["amount"]for t in transactions 
    if t["amount"]<0)
    remaining_budget = total_income + total_expenses
    print(f"\nSummary:\nTotal Income: ${total_income: .2f}")
    print(f"Total Expenses: ${abs(total_expenses):.2f}")
    print(f"Remaining Budget: ${remaining_budget: .2f}")

def view_transactions():
    if not transactions:
        print("\nNo transactions to display.")
        return
    print("n\Transactions: ")
    for t in transactions:
        print(f"{t['description']} - ${t['amount']:.2f}({t['category']})")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction(is_income = True)
        elif choice == '2':
            add_transaction(is_income = False)
        elif choice == '3':
            view_summary()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            print("Exiting tracker")
            break
        else:
            print("Please try again.")


if __name__ == "__main__":
    main()





