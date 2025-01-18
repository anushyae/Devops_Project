from expenses import expenses


def main():
    print("Starting Expense Tracker")
    expense_tracker_path = 'Expense_tracker.csv'

    # getting user inputs
    expense = getting_user_inputs()
  
    # write the expenses to file
    save_expenses(expense, expense_tracker_path)

    # Read the expenses and summarizing the balance
    read_expenses(expense_tracker_path)


def getting_user_inputs():
    expense_name = input("Please enter the Expense name: ")
    expense_amount = float(input("Please enter the Expense amount: "))
    # Getting the categories of expenses as a list
    expense_categories = ["🚗 Gas", "😎 Spending", "🛒 Groceries", "🍟 Food"]

    while True:
        print("Select a category: ")
        # Printing category one by one
        for i, category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        
        value_range = f"[1 - {len(expense_categories)}]"
        selected_value = int(input(f"Enter a number {value_range}: ")) - 1

        if selected_value in range(len(expense_categories)):
            selected_category = expense_categories[selected_value]
            new_expense = expenses(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense

        else:
            print("Invalid category. Please select a valid category") 
       

def save_expenses(expense: expenses, expense_tracker_path):
    with open(expense_tracker_path, "a", encoding='utf-8') as file:
        file.write(f"{expense.name}, {expense.category}, {expense.amount}\n")

def read_expenses(expense_tracker_path):
    with open(expense_tracker_path, "r", encoding='utf-8') as f:
        line_expenses:list[expenses] = []
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            print(expense_name, expense_category, expense_amount)
            new_expenses = expenses(name=expense_name, category=expense_category, amount=float(expense_amount) )
            line_expenses.append(new_expenses)

        amount_by_category = {}
        for ex in line_expenses:
            key = ex.category
            if key in amount_by_category:
                amount_by_category[key] += ex.amount
            else:
                amount_by_category[key] = ex.amount

        print("Expenses by category")

        for key,amount in amount_by_category.items():
            print(f"  {key} : ${amount:.2f}")


        
            
    

if __name__ == '__main__':
    main()
