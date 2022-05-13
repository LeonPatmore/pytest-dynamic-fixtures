import logging

from pytest_dynamic_fixtures.dynamic_fixture import dynamic_fixture


@dynamic_fixture(args_list=[("jack",), ("bill",)],
                 name_generator=lambda x: x,
                 fixture_params={"scope": "session"})
def generate_name_fixture(name: str) -> str:
    logging.info("Generating " + name)
    return name


def test_jack(jack):
    assert "jack" == jack


def test_jack_2(jack):
    assert "jack" == jack


def test_bill(bill):
    assert "bill" == bill
