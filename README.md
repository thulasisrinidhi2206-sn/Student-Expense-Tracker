# Student Expense Tracker

A lightweight, beginner-friendly command-line Python application designed to help students track, categorize, and analyze their expenses.

---

## Features

- **Add Expenses**: Record expenses with a description, category, and amount.
- **View All Expenses**: Display all recorded expenses in a clean tabular view.
- **Calculate Total Expenses**: View total spending across all categories.
- **Category Breakdown**: View total spending and percentages per category.
- **Average Expense**: Calculate the average spend per transaction.
- **Expense Extremes**: Identify the highest and lowest recorded expenses.
- **Input Validation**: Robust validation for positive numeric amounts and non-empty text fields.
- **Pure Python**: Zero runtime dependencies outside Python's standard library.

---

## Project Structure

```text
Student Expense Tracker/
├── tracker.py          # Core logic, functions, and CLI interface
├── test_tracker.py     # pytest unit test suite
├── requirements.txt    # Testing dependencies (pytest)
└── README.md           # Documentation and usage guide
```

---

## Getting Started

### 1. Requirements & Setup

Ensure Python 3.10+ is installed. Install testing dependencies with:

```bash
pip install -r requirements.txt
```

### 2. Running the Application

Run the tracker directly from your terminal:

```bash
python tracker.py
```

### 3. Running Unit Tests

Run the test suite using `pytest`:

```bash
python -m pytest -v
```

---

## Architecture & Functions

| Function | Description |
| :--- | :--- |
| `validate_amount(amount_input)` | Validate and return the given amount as a positive float. |
| `add_expense(expenses, description, category, amount)` | Add a new expense with description, category, and amount. |
| `calculate_total(expenses)` | Return the total amount of all expenses. |
| `calculate_by_category(expenses)` | Return total expenses grouped by category. |
| `calculate_average(expenses)` | Return the average amount of all expenses. |
| `find_extremes(expenses)` | Return the highest and lowest individual expenses. |
| `view_all_expenses(expenses)` | Return formatted lines representing all recorded expenses. |
| `print_summary(expenses)` | Print a summary and category breakdown of all expenses. |
| `main()` | Run the interactive command-line interface for the tracker. |
