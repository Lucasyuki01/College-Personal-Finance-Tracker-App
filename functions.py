import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

DATA_FILE = "sampledata.csv"

def dont_leave_without_goodbye():
    while True:
        awnser = input("Press q to quit...").lower()
        if awnser == 'q':
            break
        else:
            print('Wrong button buddy')
    clear_screen()

def clear_screen():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

# function -> 1
def view_all_transactions(df):
    print(df)
    print()
    dont_leave_without_goodbye()

# function -> 2
def view_transactions_by_date(df):
    print("=== View Transactions by Date Range ===")

    while True:
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid format for start date. Please use YYYY-MM-DD.\n")
            continue

        end_date = input("Enter the end date (YYYY-MM-DD): ")
        try:
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid format for end date. Please use YYYY-MM-DD.\n")
            continue

        if start_date_obj > end_date_obj:
            print("Start date must be earlier than or equal to end date. Please try again.\n")
            continue

        break

    print(f"\n---- Transactions from {start_date} to {end_date} ----")

    df_by_date = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)].reset_index(drop=True)

    if df_by_date.empty:
        print("No transactions found in this date range.")
    else:
        print(df_by_date)

# Helper function to capitalize only the first letter of a string
def capitalize_first_letter(text):
    # Remove leading and trailing whitespace
    text = text.strip()
    # If the string is empty, return it as is
    if not text:
        return text
    # Capitalize the first letter and make the rest lowercase
    return text[0].upper() + text[1:].lower()

# function -> 3
def add_a_transaction(df):
    # Input and validate the date
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        try:
            # Try converting the input string to a datetime object
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Input and format the category (capitalize first letter only)
    category = capitalize_first_letter(input("Enter the category of the transaction: "))

    # Input and format the description (capitalize first letter only)
    description = capitalize_first_letter(input("Enter the description of the transaction: "))

    # Input and validate the amount
    while True:
        amount = input("Enter the amount of the transaction: ")
        try:
            amount = float(amount)
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    # Input and validate the type (capitalize first letter only)
    while True:
        type_input = input("Enter the type of the transaction (Expense or Income): ")
        type_cap = capitalize_first_letter(type_input)
        if type_cap in ["Expense", "Income"]:
            type = type_cap
            break
        else:
            print("Invalid type. Please enter 'Expense' or 'Income'.")

    # Create a new row and add it to the DataFrame
    new_row = {"Date": date, "Category": category,"Description": description, "Amount": amount, "Type": type}

    df.loc[len(df)] = new_row
    print()
    print("Transaction added successfully.")
    print("You have added the following transaction")
    print()
    print(df.loc[len(df) - 1])

    # Sort the DataFrame by date
    df = df.sort_values(by=["Date"], ascending=True, ignore_index=True)
    print()

    # --- SAVE TO CSV ---
    df.to_csv(DATA_FILE, index=False)
    dont_leave_without_goodbye()

    return df

# Function to edit an existing transaction in the DataFrame
def edit_a_transaction(df):
    # Input and validate the index
    while True:
        try:
            index = int(input("Enter the index of the transaction you want to edit: "))
            if 0 <= index < len(df):
                break
            else:
                print("Index out of range.")
        except ValueError:
            print("Please enter a valid integer index.")

    print("\nCurrent Transaction Details")
    row = df.loc[index]
    print(row)
    print()

    # Input new values or press Enter to keep current ones

    # Date input and validation
    while True:
        new_date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ")
        if new_date == "":
            new_date = row["Date"]
            break
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Category input with formatting
    new_category = input("Enter new category or press Enter to keep current: ")
    new_category = capitalize_first_letter(new_category) if new_category else row["Category"]

    # Description input with formatting
    new_description = input("Enter new description or press Enter to keep current: ")
    new_description = capitalize_first_letter(new_description) if new_description else row["Description"]

    # Amount input and validation
    while True:
        new_amount = input("Enter new amount or press Enter to keep current: ")
        if new_amount == "":
            new_amount = row["Amount"]
            break
        try:
            new_amount = float(new_amount)
            if new_amount < 0:
                print("Amount cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    # Type input and validation
    while True:
        new_type = input("Enter new type (Expense or Income) or press Enter to keep current: ")
        if new_type == "":
            new_type = row["Type"]
            break
        new_type = capitalize_first_letter(new_type)
        if new_type in ["Expense", "Income"]:
            break
        else:
            print("Invalid type. Please enter 'Expense' or 'Income'.")

    # Create a new row with updated values
    new_row = {
        "Date": new_date,
        "Category": new_category,
        "Description": new_description,
        "Amount": new_amount,
        "Type": new_type
    }

    # Remove the old row
    df.drop(index, inplace=True)

    # Reset the index after dropping
    df.reset_index(drop=True, inplace=True)

    # Add the new row at the end
    df.loc[len(df)] = new_row

    # Sort the DataFrame by date
    df = df.sort_values(by=["Date"], ascending=True, ignore_index=True)

    # Show success message and updated DataFrame
    print("Transaction updated successfully.\n")
    print(df)

    df.to_csv(DATA_FILE, index=False)
    print("Transaction updated and saved.\n")
    dont_leave_without_goodbye()
    return df

# function -> 5
def delete_transaction(df):
    idx = int(input("Enter the index to delete: "))
    print("Transactions")
    print(df.loc[idx])
    print("Deleted and saved.")
    if idx in df.index:
        df.drop(idx, inplace=True)
        df.reset_index(drop=True, inplace=True)
        # df.to_csv(DATA_FILE, index=False)
    else:
        print("Invalid index.")
    print()

    dont_leave_without_goodbye()
    return df    


# function -> 6
def spending_by_category(df):
    df['Type'] = df['Type'].str.strip().str.capitalize()
    df_expenses = df[df['Type'] == 'Expense']
    grouped = (
        df_expenses
        .groupby('Category')
        .agg(Total=('Amount','sum'), Count=('Amount','count'), Average=('Amount','mean'))
        .reset_index()
    )
    total_spent = grouped['Total'].sum()
    grouped['Percent'] = grouped['Total'] / total_spent * 100

    print(grouped, "\n")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,6))
    ax1.bar(grouped['Category'], grouped['Total'])
    ax1.set_title('Total spends by category')
    ax1.set_xlabel('Category'); ax1.set_ylabel('Total spent')
    ax1.tick_params(axis='x', rotation=45)

    ax2.pie(grouped['Total'], labels=grouped['Category'], autopct='%1.1f%%')
    ax2.set_title('Expenses distribution')

    plt.tight_layout()
    plt.show()  
    dont_leave_without_goodbye()

# function -> 7
def average_monthly_spending(df):
    # Ensure Date is datetime
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])

    # Ensure Amount is numeric and Type is normalized
    df_copy['Type'] = df_copy['Type'].astype(str).str.strip().str.capitalize()
    df_copy['Amount'] = pd.to_numeric(df_copy['Amount'], errors='coerce')

    # Filter only Expenses
    expenses = df_copy[df_copy['Type'] == 'Expense'].copy()

    if expenses.empty:
        print("No expense data available.\n")
        return None, None

    # Create YearMonth column
    expenses['YearMonth'] = expenses['Date'].dt.to_period('M')

    # Group by YearMonth and sum
    monthly_totals = expenses.groupby('YearMonth')['Amount'].sum()

    # Calculate average of months with expenses (mean of totals)
    avg_per_active_month = monthly_totals.mean()

    # Calculate total / total number of months in the period
    date_range = pd.period_range(
        expenses['Date'].min().to_period('M'),
        expenses['Date'].max().to_period('M'),
        freq='M'
    )
    num_months = len(date_range)
    total_spent = expenses['Amount'].sum()
    avg_per_full_period = total_spent / num_months if num_months else 0

    print(f"Average monthly spending (active months only): CA${avg_per_active_month:.2f}")
    print(f"Average monthly spending (entire period):     CA${avg_per_full_period:.2f}\n")

    print("Monthly totals:")
    print(monthly_totals)
    print()
    dont_leave_without_goodbye()

    return avg_per_full_period, monthly_totals

# function -> 8
def top_spending_category(df):
    expenses = df[df['Type']=='Expense']
    totals_by_cat = expenses.groupby('Category')['Amount'].sum()
    top_category = totals_by_cat.idxmax()
    top_amount   = totals_by_cat.max()
    print(f"Top spending category: {top_category} — Total spent: CA${top_amount:.2f}\n")
    dont_leave_without_goodbye()
    return top_category, top_amount

# function -> 9
def visualize_monthly_spend_trend(df):
    df = df[df["Type"] == "Expense"].copy()
    df["Date"] = pd.to_datetime(df["Date"])

    monthly_sum = df.groupby(df["Date"].dt.to_period("M"))["Amount"].sum()

    print(monthly_sum)

    monthly_sum.plot(kind = "line",marker = "o")

    plt.xlabel("Month")
    plt.ylabel("Monthly Spend Sum")
    plt.title("Monthly Spend Trend")
    plt.grid(True)
    plt.show()
    dont_leave_without_goodbye()
