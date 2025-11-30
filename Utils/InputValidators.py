import re

def is_valid_date(date_str: str) -> bool:
    """
    Returns True if date_str is in YYYY-MM-DD format, otherwise False.
    """
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str))

def validate_string_size(string: str, max_length: int) -> bool:
    """
    Returns True if the string is within the specified max_length, otherwise False.
    """
    return len(string) <= max_length