from data_management import *
from data_analysis import *
from budget_management import *
from visualization import *

def display_menu() -> None:
    """Show menu options and prompt the user for a choice."""
    pass

def handle_choice(choice: int, df, budgets) -> tuple[pd.DataFrame, dict[str, float]]:
    """
    Route to the correct function based on user choice:
    import, view, add, edit, delete, analyze, budget, plot, etc.
    Returns updated (df, budgets) pair.
    """
    pass

def main():
    df = None
    budgets: dict[str, float] = {}
    while True:
        display_menu()
        choice = int(input("Enter choice (0–9): "))
        df, budgets = handle_choice(choice, df, budgets)
        if choice == 9:
            print("Exiting…")
            break

if __name__ == "__main__":
    main()
