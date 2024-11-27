import pytest
from shop import Address, User


@pytest.fixture
def fsf_address():
    return Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")


@pytest.fixture
def paris_address():
    return Address("33 quai d'Orsay", "", "Paris", "75007", "France")


@pytest.fixture
def default_user(fsf_address):
    return User(
        name="bob",
        email="bob@domain.tld",
        age=25,
        address=fsf_address,
        verified=True,
    )
