import pandas as pd
import matplotlib.pyplot as plt
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
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date   = input("Enter the end date   (YYYY-MM-DD): ")
    print(f"\n---- Transactions from {start_date} to {end_date} ----")
    subset = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)].reset_index(drop=True)
    if subset.empty:
        print("No transactions found in this date range\n")
    else:
        print(subset, "\n")
    dont_leave_without_goodbye()

# function -> 3
def add_a_transaction(df):
    date        = input("Enter the date (YYYY-MM-DD): ")
    category    = input("Enter the category of the transaction: ")
    description = input("Enter the description of the transaction: ")
    amount      = float(input("Enter the amount of the transaction: "))
    ttype       = input("Enter the type (Expense or Income): ")

    new_row = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount,
        "Type": ttype
    }
    df.loc[len(df)] = new_row
    df.sort_values(by="Date", ascending=True, ignore_index=True, inplace=True)

    # --- SAVE TO CSV ---
    df.to_csv(DATA_FILE, index=False)
    print("✅ Transaction added and saved to CSV\n")
    dont_leave_without_goodbye()
    return df

# function -> 4
def edit_transaction(df):
    index = int(input("Enter the index of the transaction you want to edit: "))
    print()
    print("Current Transaction Details")

    row = df.loc[index]

    print(row)
    print()

    new_date = input("Enter new date (YYYY-MM-DD) or press Enter to keep current:")
    new_category = input("Enter new category or press Enter to keep current:")
    new_description = input("Enter new description or press Enter to keep current:")
    new_amount = input("Enter new amount or press Enter to keep current:")
    new_type = input("Enter new type or press Enter to keep current:")

    new_date = new_date if new_date else row["Date"]
    new_category = new_category if new_category else row["Category"]
    new_description = new_description if new_description else row["Description"]
    new_amount = float(new_amount) if new_amount else row["Amount"]
    new_type = new_type if new_type else row["Type"]

    new_row = {"Date":new_date,"Category":new_category,"Description":new_description, "Amount":new_amount, "Type":new_type}

    df.drop(index, inplace = True)

    df.reset_index(inplace = True)

    df.loc[len(df)] = new_row
    df = df.sort_values(by=["Date"], ascending=True, ignore_index=True)

    print("Transaction updated successfully")
    print()
    print(df)
    dont_leave_without_goodbye()
    return df

# function -> 5
def delete_transaction(df):
    idx = int(input("Enter the index to delete: "))
    if idx in df.index:
        df.drop(idx, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(DATA_FILE, index=False)
        print("Deleted and saved.")
    else:
        print("Invalid index.")
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
