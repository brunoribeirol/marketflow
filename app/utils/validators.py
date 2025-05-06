import re
from datetime import date


def validate_name(name: str, field_name: str = "Name", min_length: int = 2) -> str:
    """
    Validates that a name is not empty and meets minimum length requirements.

    Args:
        name (str): The name to validate.
        field_name (str): Optional label for custom error messaging.
        min_length (int): Minimum acceptable length for the name.

    Returns:
        str: The cleaned and validated name.

    Raises:
        ValueError: If the name is empty or too short.
    """
    name = name.strip()
    if not name:
        raise ValueError(f"{field_name} cannot be empty.")
    if len(name) < min_length:
        raise ValueError(f"{field_name} must be at least {min_length} characters long.")
    return name


def validate_email(email: str) -> str:
    """
    Validates that an email has a proper format using regex.

    Args:
        email (str): The email to validate.

    Returns:
        str: The cleaned and validated email.

    Raises:
        ValueError: If the email format is invalid.
    """
    email = email.strip().lower()
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format.")
    return email


def validate_positive_price(price: float) -> float:
    """
    Validates that the price is a positive number.

    Args:
        price (float): The price to validate.

    Returns:
        float: The validated and rounded price.

    Raises:
        ValueError: If the price is zero or negative.
    """
    if price <= 0:
        raise ValueError("Product price must be greater than zero.")
    return round(price, 2)


def validate_id(value: int, field_name: str = "ID") -> int:
    """
    Validates that an ID is a positive integer.

    Args:
        value (int): The value to validate.
        field_name (str): Optional label for custom error messaging.

    Returns:
        int: The validated ID.

    Raises:
        ValueError: If the value is not a positive integer.
    """
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer.")
    return value


def validate_date(
    value: date, allow_future: bool = False, field_name: str = "Date"
) -> date:
    """
    Validates that a date is not in the future unless allowed.

    Args:
        value (date): The date to validate.
        allow_future (bool): Whether dates in the future are allowed.
        field_name (str): Custom field name for error messages.

    Returns:
        date: The validated date.

    Raises:
        ValueError: If date is in the future and not allowed.
    """
    if not isinstance(value, date):
        raise ValueError(f"{field_name} must be a valid date.")
    if not allow_future and value > date.today():
        raise ValueError(f"{field_name} cannot be in the future.")
    return value
