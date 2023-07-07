import re

regex = r"\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[A-Z|a-z]{2,}\b"


def check_valid_email(address):
    """Checks if the email address is valid."""
    return bool(re.fullmatch(regex, address))
