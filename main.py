import pandas as pd
from functions import *

DATA_FILE = "sampledata.csv"

def display_menu() -> None:
    print("===== Personal Finance Tracker =====\n")
    print("1. View All Transactions")
    print("2. View Transactions by Date Range")
    print("3. Add a Transaction")
    print("4. Edit a Transaction")
    print("5. Delete a Transaction")
    print("6. Analyze Spending by Category")
    print("7. Calculate Average Monthly Spending")
    print("8. Show Top Spending Category")
    print("9. Visualize Monthly Spending Trend")
    print("10. Exit\n")

def handle_choice(choice, df):
    if choice == 1:
        view_all_transactions(df)

    elif choice == 2:
        view_transactions_by_date(df)

    elif choice == 3:
        df = add_a_transaction(df)

    elif choice == 4:
        df = edit_a_transaction(df)

    elif choice == 5:
        df = delete_transaction(df)

    elif choice == 6:  
        spending_by_category(df)

    elif choice == 7:
        avg, monthly = average_monthly_spending(df)

    elif choice == 8:
        top_spending_category(df)

    elif choice == 9:
        visualize_monthly_spend_trend(df)

    elif choice == 10:
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
            choice = int(input("Choose an option (1-10): "))
        except ValueError:
            print("Please enter a number between 1 and 10.\n")
            continue

        df = handle_choice(choice, df)

if __name__ == "__main__":
    main()
