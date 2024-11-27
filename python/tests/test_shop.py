import pytest
from shop import Shop, User


@pytest.fixture
def default_user(fsf_address):
    return User(
        name="bob",
        email="bob@domain.tld",
        age=25,
        address=fsf_address,
        verified=True,
    )


def test_happy_path(default_user):
    user = default_user

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop(default_user):
    # user = User(
    #     name="bob",
    #     email="bob@domain.tld",
    #     age=16,
    #     address=fsf_address,
    #     verified=True,
    # )
    user = default_user
    user.age = 16

    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified(default_user):
    # user = User(
    #     name="bob",
    #     email="bob@domain.tld",
    #     age=16,
    #     address=fsf_address,
    #     verified=False,
    # )
    user = default_user
    user.verified = False

    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee(default_user, paris_address):
    # user = User(
    #     name="bob",
    #     email="bob@domain.tld",
    #     age=25,
    #     address=paris_address,
    #     verified=False,
    # )
    user = default_user
    user.address = paris_address

    assert Shop.must_pay_foreign_fee(user)
