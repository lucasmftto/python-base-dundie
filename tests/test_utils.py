import pytest
from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize(
    "address", ["lucas@gmail.com", "joe@dow.com", "a@b.pt"]
)
def test_positive_check_valid_email(address):
    """Test positive case for check_valid_email function"""
    assert check_valid_email(address) == True


@pytest.mark.unit
@pytest.mark.parametrize("address", ["lucas.gmail.com", "joe@dow", "a@b"])
def test_negative_check_valid_email(address):
    """Test negative case for check_valid_email function"""
    assert check_valid_email(address) == False


@pytest.mark.unit
def test_generate_simple_password():
    """Test generate_simple_password function
    TODO Generate hashed complex passwords, encrypt it
    """
    password = [generate_simple_password(8) for _ in range(100)]
    assert len(set(password)) == 100
