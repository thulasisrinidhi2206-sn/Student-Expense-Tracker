"""Student Expense Tracker.

A clean, beginner-friendly command-line application to record and analyze
student expenses with modular functions and input validation.
"""


def validate_amount(amount_input: str | float | int) -> float:
    """Validate that the given amount is a valid positive number.

    Args:
        amount_input: The input value to validate (string, float, or int).

    Returns:
        float: The validated positive amount rounded to 2 decimal places.

    Raises:
        ValueError: If amount_input is not numeric or not strictly greater than zero.
    """
    if isinstance(amount_input, str):
        cleaned = amount_input.strip()
        if not cleaned:
            raise ValueError("Amount cannot be empty.")
        try:
            amount = float(cleaned)
        except ValueError:
            raise ValueError(f"Invalid amount '{amount_input}'. Please enter a valid number.")
    elif isinstance(amount_input, (int, float)):
        amount = float(amount_input)
    else:
        raise ValueError(f"Unsupported type for amount: {type(amount_input).__name__}")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    return round(amount, 2)


def add_expense(
    expenses: list[dict], description: str, category: str, amount: float
) -> dict:
    """Add a new expense item to the expense list.

    Args:
        expenses: The list of expense records.
        description: Description of what the expense was for.
        category: Category of the expense (e.g. Food, Books, Rent).
        amount: Numeric cost of the expense.

    Returns:
        dict: The newly created expense dictionary.

    Raises:
        ValueError: If description or category are blank, or amount is invalid.
    """
    desc_clean = description.strip() if isinstance(description, str) else ""
    cat_clean = category.strip().title() if isinstance(category, str) else ""

    if not desc_clean:
        raise ValueError("Expense description cannot be empty.")
    if not cat_clean:
        raise ValueError("Expense category cannot be empty.")

    valid_amount = validate_amount(amount)

    expense = {
        "description": desc_clean,
        "category": cat_clean,
        "amount": valid_amount,
    }
    expenses.append(expense)
    return expense


def calculate_total(expenses: list[dict]) -> float:
    """Calculate the total sum of all expenses.

    Args:
        expenses: The list of expense records.

    Returns:
        float: Sum of all expenses, or 0.0 if no expenses exist.
    """
    if not expenses:
        return 0.0
    return round(sum(item["amount"] for item in expenses), 2)


def calculate_by_category(expenses: list[dict]) -> dict[str, float]:
    """Calculate total expenses grouped by category.

    Args:
        expenses: The list of expense records.

    Returns:
        dict[str, float]: Mapping of category names to their respective total amounts.
    """
    category_totals: dict[str, float] = {}
    for item in expenses:
        category = item["category"]
        category_totals[category] = round(
            category_totals.get(category, 0.0) + item["amount"], 2
        )
    return category_totals


def calculate_average(expenses: list[dict]) -> float:
    """Calculate the average amount spent per expense.

    Args:
        expenses: The list of expense records.

    Returns:
        float: The average expense amount, or 0.0 if no expenses exist.
    """
    if not expenses:
        return 0.0
    total = calculate_total(expenses)
    return round(total / len(expenses), 2)


def find_extremes(expenses: list[dict]) -> tuple[dict | None, dict | None]:
    """Find the highest and lowest individual expenses.

    Args:
        expenses: The list of expense records.

    Returns:
        tuple[dict | None, dict | None]: (highest_expense, lowest_expense),
        or (None, None) if the list is empty.
    """
    if not expenses:
        return None, None

    highest = max(expenses, key=lambda item: item["amount"])
    lowest = min(expenses, key=lambda item: item["amount"])
    return highest, lowest


def view_all_expenses(expenses: list[dict]) -> list[str]:
    """Generate human-readable lines representing all recorded expenses.

    Args:
        expenses: The list of expense records.

    Returns:
        list[str]: Formatted string list of expenses.
    """
    if not expenses:
        return ["No expenses recorded yet."]

    lines = []
    lines.append(f"{'#':<4} {'Description':<25} {'Category':<15} {'Amount':>10}")
    lines.append("-" * 58)
    for idx, item in enumerate(expenses, 1):
        lines.append(
            f"{idx:<4} {item['description']:<25} {item['category']:<15} ${item['amount']:>9.2f}"
        )
    return lines


def print_summary(expenses: list[dict]) -> None:
    """Print an analytic summary of all expenses to standard output.

    Args:
        expenses: The list of expense records.
    """
    if not expenses:
        print("\n[!] No expenses to summarize. Please add some expenses first.")
        return

    total = calculate_total(expenses)
    avg = calculate_average(expenses)
    by_cat = calculate_by_category(expenses)
    highest, lowest = find_extremes(expenses)

    print("\n" + "=" * 45)
    print("           EXPENSE SUMMARY REPORT")
    print("=" * 45)
    print(f"Total Number of Expenses: {len(expenses)}")
    print(f"Total Amount Spent:       ${total:.2f}")
    print(f"Average Expense Amount:   ${avg:.2f}")

    print("\n--- Spending by Category ---")
    for cat, cat_total in sorted(by_cat.items()):
        percentage = (cat_total / total * 100) if total > 0 else 0
        print(f"  * {cat:<15} ${cat_total:>8.2f} ({percentage:>5.1f}%)")

    print("\n--- Extremes ---")
    if highest and lowest:
        print(
            f"  * Highest Expense: {highest['description']} ({highest['category']}) - ${highest['amount']:.2f}"
        )
        print(
            f"  * Lowest Expense:  {lowest['description']} ({lowest['category']}) - ${lowest['amount']:.2f}"
        )
    print("=" * 45)


def main() -> None:
    """Interactive command-line interface for the Student Expense Tracker."""
    expenses: list[dict] = []

    print("=" * 50)
    print("   Welcome to Student Expense Tracker!")
    print("=" * 50)

    while True:
        print("\nMain Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expense Summary & Analytics")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            print("\n--- Add a New Expense ---")
            desc = input("Enter description (e.g. Textbooks): ").strip()
            if not desc:
                print("[Error] Description cannot be empty.")
                continue

            cat = input("Enter category (e.g. Books, Food, Rent, Entertainment): ").strip()
            if not cat:
                print("[Error] Category cannot be empty.")
                continue

            while True:
                amount_input = input("Enter amount ($): ").strip()
                try:
                    valid_amt = validate_amount(amount_input)
                    new_item = add_expense(expenses, desc, cat, valid_amt)
                    print(
                        f"[Success] Added: {new_item['description']} "
                        f"(${new_item['amount']:.2f}) under '{new_item['category']}'"
                    )
                    break
                except ValueError as err:
                    print(f"[Error] {err}. Please try again.")

        elif choice == "2":
            print("\n--- All Recorded Expenses ---")
            lines = view_all_expenses(expenses)
            for line in lines:
                print(line)

        elif choice == "3":
            print_summary(expenses)

        elif choice == "4":
            print("\nThank you for using Student Expense Tracker. Goodbye!")
            break

        else:
            print("[Error] Invalid choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()
