import pandas as pd
import matplotlib.pyplot as plt

def spending_by_category(df):
    df_expenses = df[df['Type'] == 'Expense']

    grouped = df_expenses.groupby('Category').agg(
        Total=('Amount', 'sum'),
        Count=('Amount', 'count'),
        Average=('Amount', 'mean')
    ).reset_index()

    total_spent = grouped['Total'].sum()
    grouped['Percent'] = grouped['Total'] / total_spent * 100

    print(grouped)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    ax1.bar(grouped['Category'], grouped['Total'])
    ax1.set_title('Total spends by category')
    ax1.set_xlabel('Category')
    ax1.set_ylabel('Total spent')
    ax1.tick_params(axis='x', rotation=45)

    ax2.pie(grouped['Total'], labels=grouped['Category'], autopct='%1.1f%%')
    ax2.set_title('Expenses distribution')

    plt.tight_layout()
    plt.show()  

def average_monthly_spending(df: pd.DataFrame) -> float:
    """Calculates the average spending per month."""
    pass

def top_spending_category(df: pd.DataFrame) -> tuple[str, float]:
    """Identifies the category with the highest spending and its amount."""
    pass
