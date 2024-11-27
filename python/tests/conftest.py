import pytest
from python.shop import Address

def fsf_address_global():
    return Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")

@pytest.fixture
def fsf_address():
    return Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")

@pytest.fixture
def paris_address():
    return Address("33 quai d'Orsay", "", "Paris", "75007", "France")

@pytest.fixture
def basic_user():
    return {'name': "bob", 'email': "bob@domain.tld"}

