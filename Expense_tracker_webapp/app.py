from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the expense class
class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

# Path to CSV file
expense_tracker_path = 'Expense_tracker.csv'

# Route to display the form and the expense summary
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user inputs from the form
        expense_name = request.form.get("name")
        expense_amount = float(request.form.get("amount"))
        selected_category = request.form.get("category")

        # Save the expense to CSV
        expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
        save_expenses(expense)

        return redirect(url_for('index'))  # Redirect back to the index page to show updated summary

    # Read the expenses and summarize the balance
    expenses_by_category, total_expense = read_expenses()

    categories = ["🚗 Gas", "😎 Spending", "🛒 Groceries", "🍟 Food"]

    return render_template("index.html", categories=categories, expenses_by_category=expenses_by_category, total_expense=total_expense)

def save_expenses(expense):
    """Append new expense to the CSV file."""
    file_exists = os.path.exists(expense_tracker_path)
    with open(expense_tracker_path, "a", encoding='utf-8') as file:
        if not file_exists:
            file.write("Name,Category,Amount\n")  # Write header if file doesn't exist
        file.write(f"{expense.name},{expense.category},{expense.amount}\n")

def read_expenses():
    """Read expenses from the CSV file and summarize by category."""
    with open(expense_tracker_path, "r", encoding='utf-8') as file:
        line_expenses = []
        lines = file.readlines()
        for line in lines[1:]:  # Skip header line
            expense_name, expense_category, expense_amount = line.strip().split(",")
            expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            line_expenses.append(expense)

        amount_by_category = {}
        for ex in line_expenses:
            if ex.category in amount_by_category:
                amount_by_category[ex.category] += ex.amount
            else:
                amount_by_category[ex.category] = ex.amount

        total_expense = sum(amount_by_category.values())

        return amount_by_category, total_expense

if __name__ == "__main__":
    app.run(debug=True)
