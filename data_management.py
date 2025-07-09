import pandas as pd

def import_transactions(file_path: str) -> pd.DataFrame:
    """
    Reads a CSV of transactions and returns a DataFrame.
    — Checks for format errors / missing columns.
    """
    pass

def view_all_transactions(df: pd.DataFrame) -> None:
    """Displays all transactions."""
    pass

def view_transactions_by_date(df: pd.DataFrame, start: str, end: str) -> None:
    """Filters and displays transactions between two dates (YYYY-MM-DD)."""
    pass

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

def delete_transaction(df: pd.DataFrame, index: int) -> pd.DataFrame:
    """Removes a transaction by index and returns the updated DataFrame."""
    pass
