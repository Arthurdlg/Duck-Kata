from python.shop import User, Shop, Address
from python.tests.conftest import basic_user, fsf_address_global


class UserBuilder:
    """
    Builder pour construire des objets User de manière fluide et flexible.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self._name = "bob"
        self._email = "bob@domain.tld"
        self._age = 25
        self._verified = True
        self._address = fsf_address_global()

    def with_name(self, name: str):
        self._name = name
        return self

    def with_email(self, email: str):
        self._email = email
        return self

    def with_age(self, age: int):
        self._age = age
        return self

    def with_verified(self, verified: bool):
        self._verified = verified
        return self

    def with_address(self, address: Address):
        self._address = address
        return self

    def build(self) -> User:
        return User(
            name=self._name,
            email=self._email,
            age=self._age,
            address=self._address,
            verified=self._verified,
        )


def test_happy_building(fsf_address, basic_user):
    user = UserBuilder().build()
    assert user

def test_cannot_order_user_under_18():
    user = UserBuilder().with_age(17).build()
    assert Shop.can_order(user) is False

def test_cannot_order_unverified_user():
    user = UserBuilder().with_verified(False).build()
    assert Shop.can_order(user) is False

def test_user_must_pay_foreign_fee_if_non_usa(paris_address):
    user = UserBuilder().with_address(paris_address).build()
    assert Shop.must_pay_foreign_fee(user) is True