#Matheus H Hipolito
#09-16-2024
#This program ask for user monthly expenses, asks for the type of expense and amount, and display the total expenses, from
#highest to lowest:

from functools import reduce  # Import the reduce function

def main():
    expenses = []

    # Collect user input for expenses
    while True:
        expense_type = input("Enter the type of expense (or type 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            # Get the amount for the expense
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Please enter a valid number for the amount.")

    if not expenses:
        print("No expenses entered.")
        return

    # Function to accumulate total expense
    def add_expenses(acc, expense):
        return acc + expense[1]

    # Function to find the maximum expense
    def find_max(expense1, expense2):
        return expense1 if expense1[1] > expense2[1] else expense2

    # Function to find the minimum expense
    def find_min(expense1, expense2):
        return expense1 if expense1[1] < expense2[1] else expense2

    # Calculate total expense using reduce
    total_expense = reduce(add_expenses, expenses, 0)

    # Find the highest expense using reduce
    highest_expense = reduce(find_max, expenses)

    # Find the lowest expense using reduce
    lowest_expense = reduce(find_min, expenses)

    # Show results
    print(f"Total expense: ${total_expense:.2f}")
    print(f"Highest expense: ${highest_expense[1]:.2f} for {highest_expense[0]}")
    print(f"Lowest expense: ${lowest_expense[1]:.2f} for {lowest_expense[0]}")

if __name__ == "__main__":
    main()
