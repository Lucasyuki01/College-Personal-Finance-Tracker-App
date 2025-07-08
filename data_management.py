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

def add_transaction(df: pd.DataFrame, date: str, category: str, description: str, amount: float) -> pd.DataFrame:
    """Adds a transaction and returns the updated DataFrame."""
    pass

def edit_transaction(df: pd.DataFrame, index: int, **kwargs) -> pd.DataFrame:
    """
    Edits fields of an existing transaction.
    kwargs may include date, category, description, amount.
    """
    pass

def delete_transaction(df: pd.DataFrame, index: int) -> pd.DataFrame:
    """Removes a transaction by index and returns the updated DataFrame."""
    pass
