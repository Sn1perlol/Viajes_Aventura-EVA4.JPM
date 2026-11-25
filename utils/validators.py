import os
import re

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def request_data(prompt, validator):
    """Loops until the user enters valid data based on the validator function."""
    while True:
        try:
            value = input(prompt)
            return validator(value)
        except ValueError as e:
            print(f"Error: {e}. Try again.")

def validate_email(email):
    """Validates the email format and returns it in lowercase."""
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email.strip()):
        raise ValueError("Invalid email format.")
    return email.strip().lower()

def validate_positive_int(value, field_name="Number"):
    """Validates that the input is an integer greater than zero."""
    try:
        num = int(value)
        if num <= 0:
            raise ValueError(f"{field_name} must be greater than zero.")
        return num
    except ValueError:
        raise ValueError(f"{field_name} must be a valid integer.")

def validate_positive_float(value, field_name="Amount"):
    """Validates that the input is a float greater than or equal to zero."""
    try:
        num = float(value)
        if num < 0:
            raise ValueError(f"{field_name} cannot be negative.")
        return num
    except ValueError:
        raise ValueError(f"{field_name} must be a valid number.")

def validate_required(value, field_name="Field"):
    """Validates that the input is not empty."""
    if not value or not value.strip():
        raise ValueError(f"{field_name} is required.")
    return value.strip()