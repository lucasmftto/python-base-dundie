from random import sample
from string import ascii_letters, digits


def generate_simple_password(size=8):
    """Generate a simple password with a given length
    Args:
        length (int): Length of the password
    Returns:
        str: password
    """
    return "".join(sample(ascii_letters + digits, size))
