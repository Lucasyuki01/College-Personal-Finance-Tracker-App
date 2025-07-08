import pandas as pd

def set_budget(category: str, amount: float) -> None:
    """Set a monthly budget for a given category."""
    pass

def get_budget(category: str) -> float:
    """Retrieve the budget amount for the specified category."""
    pass

def view_budgets() -> dict[str, float]:
    """Return all budgets as a mapping of category to amount."""
    pass

def check_budget_status(df: pd.DataFrame, budgets: dict[str, float]) -> pd.DataFrame:
    """
    Compare actual spending against budgets.
    Return a DataFrame with columns: category, budgeted, actual, difference.
    """
    pass
