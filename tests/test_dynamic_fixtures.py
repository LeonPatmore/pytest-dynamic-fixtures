import logging

from pytest_dynamic_fixtures.dynamic_fixture import dynamic_fixture


@dynamic_fixture(args_list=[("jack", "castleton"), ("bill", "allen")],
                 name_generator=lambda x, _: x,
                 fixture_params={"scope": "session"})
def generate_surname_fixture(_: str, surname: str) -> str:
    return surname


@dynamic_fixture(args_list=[("jack",), ("bill",)],
                 name_generator=lambda x: f"{x}_surname_length",
                 fixtures=["request"])
def generate_surname_length(name: str, request):
    surname = request.getfixturevalue(name)
    return len(surname)


def test_jack(jack):
    assert "castleton" == jack


def test_bill(bill):
    assert "allen" == bill


def test_bill_value(bill_surname_length):
    assert 5 == bill_surname_length


def test_jack_value(jack_surname_length):
    assert 9 == jack_surname_length
