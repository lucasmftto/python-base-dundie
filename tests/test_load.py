import pytest
from dundie.core import load
from .constants import PEOPLE_FILE


def setup_module(module):
    print('Roda antes do módulo')
    
def teardown_module(module):
    print('Roda depois do módulo')
    
    
@pytest.mark.unit
def test_load(request):
    
    request.addfinalizer(lambda: print('Roda depois do teste'))
    
    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == 'L'
