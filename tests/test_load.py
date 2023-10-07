import pytest
from dundie.core import load

from .constants import PEOPLE_FILE


def setup_module(module):
    print("Roda antes do módulo")


def teardown_module(module):
    print("Roda depois do módulo")


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people(request):
    """Test function load function."""
    assert len(load(PEOPLE_FILE)) == 3


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_j(request):
    """Test function load function."""
    assert load(PEOPLE_FILE)[0]["name"] == "Lucas Favaretto"
