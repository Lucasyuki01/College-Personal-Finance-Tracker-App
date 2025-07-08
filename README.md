# Personal Finance Tracker

A simple command-line tool to import, view, analyze and visualize your personal transactions, plus set and monitor monthly budgets by category.

## Features

* **Import & manage** transactions in CSV format
* **View** all transactions or filter by date range
* **Basic analysis**: total spending per category, average monthly spend, top category
* **Budgets**: set, view and compare actual vs. budgeted spending
* **Plots**: line chart for monthly trend, bar chart by category, pie chart distribution
* **Interactive CLI**: menu-driven interface to tie it all together

## Project Structure

```
personal_finance_tracker/
│
├── budget_management.py      # budget CRUD and status checks
├── data_analysis.py         # spending calculations
├── data_management.py       # CSV import, CRUD for transactions
├── main.py                  # CLI entry point
├── sampledata.csv           # example dataset
├── requirements.txt         # Python dependencies
├── README.md                # this document
└── visualization.py         # plotting routines
```

## Prerequisites

* Python 3.8+
* pip (or your preferred package manager)

## Installation

1. Clone this repo:

   ```bash
   git clone https://github.com/your-username/personal-finance-tracker.git
   cd personal-finance-tracker
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Prepare a CSV (see `sampledata.csv` for format):

   ```csv
   date,category,description,amount
   2025-07-01,Food,Lunch at cafe,12.50
   2025-07-02,Transport,Bus fare,3.00
   ```

2. Run the CLI:

   ```bash
   python main.py
   ```

3. Follow the on-screen menu to:

   * **Import** your CSV
   * **View** or **filter** transactions
   * **Add**, **edit** or **delete** entries
   * **Perform analysis** (spending by category, average, top)
   * **Set budgets** and **check budget status**
   * **Generate plots** (monthly trend, category breakdown, distribution)
   * **Exit** when you’re done

## Module Overview

* **`data_management.py`**

  * `import_transactions`
  * `view_all_transactions`
  * `view_transactions_by_date`
  * `add_transaction` / `edit_transaction` / `delete_transaction`

* **`data_analysis.py`**

  * `spending_by_category`
  * `average_monthly_spending`
  * `top_spending_category`

* **`budget_management.py`**

  * `set_budget` / `get_budget` / `view_budgets`
  * `check_budget_status`

* **`visualization.py`**

  * `plot_monthly_trend`
  * `plot_spending_by_category`
  * `plot_spending_distribution`

* **`main.py`**

  * `display_menu` / `handle_choice`
  * Coordinates all modules in a simple text menu loop

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m "Add awesome feature"`)
4. Push to your branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

Please ensure your code is well-documented and includes basic tests where appropriate.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
