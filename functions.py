import pandas as pd
import matplotlib.pyplot as plt

# function -> 1
def view_all_transactions(df):
    print(df)
    print()

# function -> 2
def view_transactions_by_date(df):
    start_date = input("Enter the start date(YYYY-MM-DD): ")
    end_date = input("Enter the end date(YYYY-MM-DD): ")
    print()
    print("----Transactions from", start_date, "to", end_date,"----")

    df_by_date = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)].reset_index(drop=True)
    if df_by_date.empty:
        print("No transactions found in this date range")
    else:
        print(df_by_date)
    print()

# function -> 3
def add_a_transaction(df):
    date = input("Enter the date(YYYY-MM-DD): ")
    category = input("Enter the category of the transaction: ")
    description = input("Enter the description of the transaction: ")
    amount = input("Enter the amount of the transaction: ")
    type = input("Enter the type of the transaction(Expense or Income): ")

    new_row = {"Date":date,"Category":category,"Description":description, "Amount":amount, "Type":type}
    df.loc[len(df)] = new_row
    df = df.sort_values(by = ["Date"],ascending = True, ignore_index = True)
    print("Transaction added successfully")
    print(df)
    print()
    return df

# function -> 4
def edit_transaction():
    """
    Edits fields of an existing transaction.
    kwargs may include date, category, description, amount.
    """
    pass

# function -> 5
def delete_transaction(df):
    awnser = int(input("Enter the index of the transaction to delete: "))
    df.drop(awnser, axis='index', inplace=True)
    print()

# function -> 6
def spending_by_category(df):
    df_expenses = df[df['Type'] == 'Expense']

    grouped = df_expenses.groupby('Category').agg(
        Total=('Amount', 'sum'),
        Count=('Amount', 'count'),
        Average=('Amount', 'mean')
    ).reset_index()

    total_spent = grouped['Total'].sum()
    grouped['Percent'] = grouped['Total'] / total_spent * 100

    print(grouped)
    print()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    ax1.bar(grouped['Category'], grouped['Total'])
    ax1.set_title('Total spends by category')
    ax1.set_xlabel('Category')
    ax1.set_ylabel('Total spent')
    ax1.tick_params(axis='x', rotation=45)

    ax2.pie(grouped['Total'], labels=grouped['Category'], autopct='%1.1f%%')
    ax2.set_title('Expenses distribution')

    plt.tight_layout()
    plt.show()  

# function -> 7
def average_monthly_spending(df):
    
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])

    expenses = df_copy[df_copy['Type'] == 'Expense'].copy()

    expenses['YearMonth'] = expenses['Date'].dt.to_period('M')

    monthly_totals = expenses.groupby('YearMonth')['Amount'].sum()

    avg_spending = monthly_totals.mean()

    print(f"Average monthly spending CA${avg_spending:.2f}")
    print()

# function -> 8
def top_spending_category(df):
    df_copy = df.copy()

    expenses = df_copy[df_copy['Type'] == 'Expense']
    totals_by_cat = expenses.groupby('Category')['Amount'].sum()
    top_category = totals_by_cat.idxmax()
    top_amount = totals_by_cat.max()

    print(f"Top spending category: {top_category} — Total spent: CA${top_amount:.2f}")
    print()

#function -> 9
def visualize_monthly_spending_trend():
    pass

def set_budget():
    """Set a monthly budget for a given category."""

def get_budget():
    """Retrieve the budget amount for the specified category."""

def view_budgets():
    """Return all budgets as a mapping of category to amount."""

def check_budget_status():
    """
    Compare actual spending against budgets.
    Return a DataFrame with columns: category, budgeted, actual, difference.
    """
    pass