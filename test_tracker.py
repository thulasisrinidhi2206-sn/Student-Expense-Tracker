"""Unit tests for the Student Expense Tracker application."""

import pytest
from tracker import (
    add_expense,
    calculate_average,
    calculate_by_category,
    calculate_total,
    find_extremes,
    validate_amount,
    view_all_expenses,
)


# =====================================================================
# Tests for validate_amount
# =====================================================================


def test_validate_amount_valid_string_integer():
    """Test valid integer passed as string."""
    assert validate_amount("25") == 25.0


def test_validate_amount_valid_string_float():
    """Test valid float passed as string."""
    assert validate_amount("12.75") == 12.75


def test_validate_amount_valid_numeric_types():
    """Test valid numeric types (int and float)."""
    assert validate_amount(100) == 100.0
    assert validate_amount(45.99) == 45.99


def test_validate_amount_whitespace_handling():
    """Test string with leading and trailing whitespaces."""
    assert validate_amount("  89.50 \t\n") == 89.50


def test_validate_amount_rounding():
    """Test rounding to two decimal places."""
    assert validate_amount("10.999") == 11.00
    assert validate_amount(10.126) == 10.13


def test_validate_amount_zero():
    """Test that zero amount raises ValueError."""
    with pytest.raises(ValueError, match="greater than zero"):
        validate_amount("0")
    with pytest.raises(ValueError, match="greater than zero"):
        validate_amount(0)


def test_validate_amount_negative():
    """Test that negative amounts raise ValueError."""
    with pytest.raises(ValueError, match="greater than zero"):
        validate_amount("-15.50")
    with pytest.raises(ValueError, match="greater than zero"):
        validate_amount(-10)


def test_validate_amount_non_numeric_string():
    """Test that invalid non-numeric strings raise ValueError."""
    with pytest.raises(ValueError, match="valid number"):
        validate_amount("abc")
    with pytest.raises(ValueError, match="valid number"):
        validate_amount("$50")


def test_validate_amount_empty_string():
    """Test that empty or blank strings raise ValueError."""
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_amount("")
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_amount("   ")


def test_validate_amount_unsupported_type():
    """Test that passing unsupported types raises ValueError."""
    with pytest.raises(ValueError, match="Unsupported type"):
        validate_amount(None)  # type: ignore
    with pytest.raises(ValueError, match="Unsupported type"):
        validate_amount(["100"])  # type: ignore


# =====================================================================
# Tests for add_expense
# =====================================================================


def test_add_expense_success():
    """Test adding a valid expense."""
    expenses = []
    created = add_expense(expenses, "Notebook", "stationery", 5.50)

    assert len(expenses) == 1
    assert created == {
        "description": "Notebook",
        "category": "Stationery",
        "amount": 5.50,
    }
    assert expenses[0] == created


def test_add_expense_multiple():
    """Test adding multiple expenses."""
    expenses = []
    add_expense(expenses, "Lunch", "Food", 12.00)
    add_expense(expenses, "Bus Ticket", "Transport", "3.50")

    assert len(expenses) == 2
    assert expenses[0]["description"] == "Lunch"
    assert expenses[1]["amount"] == 3.50


def test_add_expense_empty_description():
    """Test that empty description raises ValueError."""
    expenses = []
    with pytest.raises(ValueError, match="description cannot be empty"):
        add_expense(expenses, "   ", "Food", 10.0)


def test_add_expense_empty_category():
    """Test that empty category raises ValueError."""
    expenses = []
    with pytest.raises(ValueError, match="category cannot be empty"):
        add_expense(expenses, "Textbook", "", 45.0)


def test_add_expense_invalid_amount():
    """Test that invalid amount raises ValueError and does not add expense."""
    expenses = []
    with pytest.raises(ValueError):
        add_expense(expenses, "Coffee", "Food", -4.00)
    assert len(expenses) == 0


# =====================================================================
# Tests for calculate_total
# =====================================================================


def test_calculate_total_empty():
    """Test calculating total on empty expense list."""
    assert calculate_total([]) == 0.0


def test_calculate_total_single():
    """Test calculating total with a single expense."""
    expenses = [{"description": "Coffee", "category": "Food", "amount": 4.75}]
    assert calculate_total(expenses) == 4.75


def test_calculate_total_multiple():
    """Test calculating total with multiple expenses and floating point precision."""
    expenses = [
        {"description": "Book", "category": "Education", "amount": 29.99},
        {"description": "Lunch", "category": "Food", "amount": 10.01},
        {"description": "Bus", "category": "Transport", "amount": 5.25},
    ]
    assert calculate_total(expenses) == 45.25


# =====================================================================
# Tests for calculate_by_category
# =====================================================================


def test_calculate_by_category_empty():
    """Test category breakdown for empty expense list."""
    assert calculate_by_category([]) == {}


def test_calculate_by_category_grouped():
    """Test category breakdown grouping multiple items correctly."""
    expenses = [
        {"description": "Coffee", "category": "Food", "amount": 4.50},
        {"description": "Sandwich", "category": "Food", "amount": 8.50},
        {"description": "Notebook", "category": "Supplies", "amount": 12.00},
        {"description": "Subway Pass", "category": "Transport", "amount": 25.00},
    ]
    result = calculate_by_category(expenses)
    assert result == {
        "Food": 13.00,
        "Supplies": 12.00,
        "Transport": 25.00,
    }


# =====================================================================
# Tests for calculate_average
# =====================================================================


def test_calculate_average_empty():
    """Test calculating average on empty expense list."""
    assert calculate_average([]) == 0.0


def test_calculate_average_single():
    """Test calculating average with single expense."""
    expenses = [{"description": "Rent", "category": "Housing", "amount": 350.00}]
    assert calculate_average(expenses) == 350.00


def test_calculate_average_multiple():
    """Test calculating average with multiple expenses."""
    expenses = [
        {"description": "Item 1", "category": "Cat", "amount": 10.00},
        {"description": "Item 2", "category": "Cat", "amount": 20.00},
        {"description": "Item 3", "category": "Cat", "amount": 30.00},
    ]
    assert calculate_average(expenses) == 20.00


def test_calculate_average_rounding():
    """Test average rounding to two decimal places."""
    expenses = [
        {"description": "Item 1", "category": "Cat", "amount": 10.00},
        {"description": "Item 2", "category": "Cat", "amount": 20.00},
    ]  # (10 + 20) / 2 = 15.00
    assert calculate_average(expenses) == 15.00

    expenses_fractional = [
        {"description": "Item 1", "category": "Cat", "amount": 10.00},
        {"description": "Item 2", "category": "Cat", "amount": 10.00},
        {"description": "Item 3", "category": "Cat", "amount": 11.00},
    ]  # 31 / 3 = 10.3333... -> 10.33
    assert calculate_average(expenses_fractional) == 10.33


# =====================================================================
# Tests for find_extremes
# =====================================================================


def test_find_extremes_empty():
    """Test finding extremes on empty expense list."""
    highest, lowest = find_extremes([])
    assert highest is None
    assert lowest is None


def test_find_extremes_single():
    """Test finding extremes on a list with one item."""
    single = {"description": "Tuition", "category": "Education", "amount": 500.00}
    highest, lowest = find_extremes([single])
    assert highest == single
    assert lowest == single


def test_find_extremes_multiple():
    """Test finding extremes with distinct amounts."""
    item1 = {"description": "Pen", "category": "Supplies", "amount": 1.99}
    item2 = {"description": "Groceries", "category": "Food", "amount": 65.50}
    item3 = {"description": "Lab Manual", "category": "Education", "amount": 18.00}
    expenses = [item1, item2, item3]

    highest, lowest = find_extremes(expenses)
    assert highest == item2
    assert lowest == item1


# =====================================================================
# Tests for view_all_expenses
# =====================================================================


def test_view_all_expenses_empty():
    """Test formatting for empty expense list."""
    output = view_all_expenses([])
    assert output == ["No expenses recorded yet."]


def test_view_all_expenses_populated():
    """Test formatting for populated expense list."""
    expenses = [
        {"description": "Textbook", "category": "Education", "amount": 85.00},
        {"description": "Dinner", "category": "Food", "amount": 15.50},
    ]
    lines = view_all_expenses(expenses)
    assert len(lines) == 4  # Header + separator + 2 data rows
    assert "Textbook" in lines[2]
    assert "$    85.00" in lines[2]
    assert "Dinner" in lines[3]
    assert "$    15.50" in lines[3]
