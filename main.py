import pandas as pd
from functions import *

DATA_FILE = "sampledata.csv"

def display_menu() -> None:
    print("===== Personal Finance Tracker =====\n")
    print("1. View All Transactions (Add/Edit/Delete)")
    print("2. View Transactions by Date Range")
    print("3. Analyze Spending by Category")
    print("4. Calculate Average Monthly Spending")
    print("5. Show Top Spending Category")
    print("6. Visualize Monthly Spending Trend")
    print("7. Exit\n")

def handle_choice(choice, df):
    if choice == 1:
        df = view_all_transactions(df)

    elif choice == 2:
        view_transactions_by_date(df)

    elif choice == 3:
        spending_by_category(df)

    elif choice == 4:
        avg, monthly = average_monthly_spending(df)

    elif choice == 5:
        top_spending_category(df)

    elif choice == 6:
        visualize_monthly_spend_trend(df)

    elif choice == 7:
        print("Goodbye!")
        exit()

    else:
        print("Invalid choice. Try again.\n")

    return df

def main():
    df = pd.read_csv(DATA_FILE)
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option (1-7): "))
        except ValueError:
            print("Please enter a number between 1 and 7.\n")
            continue

        df = handle_choice(choice, df)

if __name__ == "__main__":
    main()