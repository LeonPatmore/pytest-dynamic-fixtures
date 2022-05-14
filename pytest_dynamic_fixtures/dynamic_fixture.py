import inspect

import pytest


class FunctionWithArgs:

    def __init__(self, func: callable, fixtures: list, args: tuple):
        self.func = func
        self.args = args
        self.fixtures = fixtures

    def get(self, fixture_values: dict):
        return self.func(*self.args, **fixture_values)


def gen_fix_outside(func_with_args: FunctionWithArgs, fixture_params: dict):
    @pytest.fixture(**fixture_params)
    def gen_fix(request):

        fixture_values = {}
        for fixture_name in func_with_args.fixtures:
            fixture_values[fixture_name] = request.getfixturevalue(fixture_name)

        val = func_with_args.get(fixture_values)
        return val
    return gen_fix


def dynamic_fixture(args_list: list,
                    name_generator: callable,
                    fixture_params: dict = None,
                    fixtures: list = None):
    if fixture_params is None:
        fixture_params = {}
    if fixtures is None:
        fixtures = []

    def dynamic_fixture_for_params(func):
        module = inspect.getmodule(func)
        for this_args in args_list:
            func_with_args = FunctionWithArgs(func, fixtures, this_args)
            setattr(module, name_generator(*this_args), gen_fix_outside(func_with_args, fixture_params))

        def pass_f():
            pass
        return pass_f
    return dynamic_fixture_for_params
