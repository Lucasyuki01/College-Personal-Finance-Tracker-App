import pandas as pd
import matplotlib.pyplot as plt

# Change this if your CSV lives elsewhere:
DATA_FILE = "sampledata.csv"


def view_all_transactions(df):
    print(df, "\n")


def view_transactions_by_date(df):
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date   = input("Enter the end date   (YYYY-MM-DD): ")
    print(f"\n---- Transactions from {start_date} to {end_date} ----")
    subset = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)].reset_index(drop=True)
    if subset.empty:
        print("No transactions found in this date range\n")
    else:
        print(subset, "\n")


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
    return df


def edit_transaction(df):
    """
    Example: edit one field of a transaction by index.
    """
    idx = int(input("Enter the index of the transaction to edit: "))
    if idx not in df.index:
        print("⚠️  Invalid index\n")
        return df

    print("Current row:")
    print(df.loc[[idx]], "\n")

    field = input("Which field to edit? (Date/Category/Description/Amount/Type): ")
    if field not in df.columns:
        print("⚠️  Unknown field\n")
        return df

    new_value = input(f"Enter new value for {field}: ")
    # convert amount to float if needed
    if field == "Amount":
        new_value = float(new_value)

    df.at[idx, field] = new_value

    # --- SAVE TO CSV ---
    df.to_csv(DATA_FILE, index=False)
    print("✅ Transaction edited and saved to CSV\n")
    return df


def delete_transaction(df):
    idx = int(input("Enter the index to delete: "))
    if idx in df.index:
        df.drop(idx, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(DATA_FILE, index=False)
        print("Deleted and saved.")
    else:
        print("Invalid index.")
    return df    


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


def average_monthly_spending(df):
    df_copy = df.copy()
    df_copy['Date'] = pd.to_datetime(df_copy['Date'])
    expenses = df_copy[df_copy['Type']=='Expense'].copy()
    expenses['YearMonth'] = expenses['Date'].dt.to_period('M')
    monthly_totals = expenses.groupby('YearMonth')['Amount'].sum()
    avg_spending = monthly_totals.mean()
    print(f"Average monthly spending: CA${avg_spending:.2f}\n")
    return avg_spending, monthly_totals


def top_spending_category(df):
    expenses = df[df['Type']=='Expense']
    totals_by_cat = expenses.groupby('Category')['Amount'].sum()
    top_category = totals_by_cat.idxmax()
    top_amount   = totals_by_cat.max()
    print(f"Top spending category: {top_category} — Total spent: CA${top_amount:.2f}\n")
    return top_category, top_amount


def visualize_monthly_spending_trend(df):
    """
    You could implement a line plot here.
    """
    pass
