from data_management import *
from data_analysis import *
from budget_management import *
from visualization import *

def display_menu() -> None:
    print("===== Personal Finance Tracker =====")
    print()
    
    print("1. View All Transactions")
    print("2. View Transactions by Date Range")
    print("3. Add a Transaction")
    print("4. Edit a Transaction")
    print("5. Delete a Transaction")
    print("6. Analyze Spending by Category")
    print("7. Calculate Average Monthly Spending")
    print("8. Show Top Spending Category")
    print("9. Visualize Monthly Spending Trend")
    print("10. Exit")
    print()

def handle_choice(choice, df):
    if choice == 1:
        view_all_transactions()

    elif choice == 2:
        view_transactions_by_date()
    
    elif choice == 3:
        add_a_transaction()

    elif choice == 4:
        edit_transaction()

    elif choice == 5:
        delete_transaction(df)

    elif choice == 6:
        spending_by_category(df)

    elif choice == 7:
        calculate_average_monthly()

    elif choice == 8:
        show_top_spending_category()

    elif choice == 9:
        visualize_monthly_spending_trend()

    elif choice == 10:
        exit()

def main():
    df = pd.read_csv("sampledata.csv")

    while True:
        display_menu()
        choice = int(input(f"Choose an option (1-10): "))
        handle_choice(choice, df)

if __name__ == "__main__":
    main()
