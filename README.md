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
| `validate_amount(amount_input)` | Validates numeric inputs, handles rounding, and enforces values > 0. |
| `add_expense(expenses, description, category, amount)` | Creates and stores a new expense dictionary record. |
| `calculate_total(expenses)` | Computes the sum of all recorded expenses. |
| `calculate_by_category(expenses)` | Aggregates expense totals grouped by category. |
| `calculate_average(expenses)` | Computes the average expense value. |
| `find_extremes(expenses)` | Identifies the highest and lowest expense records. |
| `view_all_expenses(expenses)` | Generates formatted rows for table display. |
| `print_summary(expenses)` | Generates a complete analytics breakdown report. |
| `main()` | CLI interactive menu loop. |
