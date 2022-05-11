import pytest


NAMES = ["jack", "bill", "peter"]


def per_name_generator(name: str):

    @pytest.fixture(scope="session")
    def generate_name() -> str:
        return name

    return generate_name


for name in NAMES:
    globals()[name] = per_name_generator(name)


def test_jack(jack):
    assert "jack" == jack


def test_bill(bill):
    assert "bill" == bill
