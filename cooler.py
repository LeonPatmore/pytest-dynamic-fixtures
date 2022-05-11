import functools

import pytest


NAMES = ["jack", "bill", "peter"]


# class FunctionHolder:
#
#     def __init__(self, func, *args):
#         self.func = func
#         self.args = args
#
#     def get(self):
#         return self.func(*self.args)
#
#
# def fixture_per_name(func):
#
#     for name in NAMES:
#         func_holder = FunctionHolder(func, name)
#
#         @pytest.fixture(scope="session")
#         def generate_name():
#             return func_holder.get()
#
#         print("setting fixture with name " + name)
#         globals()[name] = generate_name
#
#     def pass_f():
#         pass
#     return pass_f
#
#
# @fixture_per_name
class A:

    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def get(self):
        return self.func(*self.args)


def gen_fix_outside(a_class: A):
    @pytest.fixture(scope="session")
    def gen_fix():
        val = a_class.get()
        return val
    return gen_fix


def fixture_per_name_factory(fix_name_gen: callable):
    def fixture_per_name(func):
        for name in NAMES:
            print("setting fixture with name " + name)
            a_class = A(func, name)
            globals()[fix_name_gen(name)] = gen_fix_outside(a_class)
        def pass_f():
            pass
        return pass_f
    return fixture_per_name


@fixture_per_name_factory(lambda x: x)
def generate_name(name: str) -> str:
    return name


@fixture_per_name_factory(lambda x: f"{x}_cost")
def generate_name_costs(name: str) -> int:
    return {
        "jack": 1,
        "bill": 2
    }[name]


def test_jack(jack):
    assert "jack" == jack


def test_jack_cost(jack_cost):
    assert 1 == jack_cost


def test_bill(bill):
    assert "bill" == bill


def test_bill_cost(bill_cost):
    assert 2 == bill_cost
