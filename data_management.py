import pandas as pd

def import_transactions(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV of transactions and returns a DataFrame.
    — Checks for format errors / missing columns.
    """
    pass

def view_all_transactions(df):
    print(df)

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
    return df


def edit_transaction(df: pd.DataFrame, index: int, **kwargs) -> pd.DataFrame:
    """
    Edits fields of an existing transaction.
    kwargs may include date, category, description, amount.
    """
    pass

def delete_transaction(df):
    awnser = int(input("Enter the index of the transaction to delete: "))
    df.drop(awnser, axis='index', inplace=True)