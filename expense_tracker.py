import csv
from pathlib import Path

FILE_NAME = Path("expenses.csv")
FIELDNAMES = ["date", "item", "category", "amount"]


def load_expenses():
    """Load saved expenses. Start with an empty list if the file is missing."""
    try:
        with FILE_NAME.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    """Write all expenses to the CSV file."""
    with FILE_NAME.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    date = input("Enter date (e.g. 2026-11-14): ").strip()
    item = input("Enter item name: ").strip()
    category = input("Enter category (e.g. Stationery): ").strip().title()

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number, such as 250 or 250.50.")

    expenses.append({
        "date": date,
        "item": item,
        "category": category,
        "amount": f"{amount:.2f}"
    })
    save_expenses(expenses)
    print("Expense saved successfully.")


def show_expenses(expenses):
    if not expenses:
        print("No expense records found.")
        return

    print("\nDATE         ITEM                 CATEGORY             AMOUNT")
    print("-" * 68)
    for expense in expenses:
        print(
            f"{expense['date']:<12} "
            f"{expense['item']:<20} "
            f"{expense['category']:<20} "
            f"{float(expense['amount']):>8.2f}"
        )

    categories = {expense["category"] for expense in expenses}
    print("\nUnique categories:", ", ".join(sorted(categories)))


def total_by_category(expenses):
    if not expenses:
        print("No expenses available to calculate.")
        return

    categories = {expense["category"] for expense in expenses}
    print("\nTotal expenses by category:")
    for category in sorted(categories):
        total = sum(
            float(expense["amount"])
            for expense in expenses
            if expense["category"] == category
        )
        print(f"{category}: {total:.2f}")


def main():
    expenses = load_expenses()
    print(f"Loaded {len(expenses)} saved expense record(s).")

    while True:
        print("\n===== INSTITUTE EXPENSE TRACKER =====")
        print("1. Add New Expense")
        print("2. Show All Expenses")
        print("3. Calculate Total Expenses by Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
