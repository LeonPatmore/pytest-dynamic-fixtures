import inspect

import pytest


class FunctionWithArgs:

    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def get(self):
        return self.func(*self.args)


def gen_fix_outside(func_with_args: FunctionWithArgs, fixture_params: dict):
    @pytest.fixture(**fixture_params)
    def gen_fix():
        val = func_with_args.get()
        return val
    return gen_fix


def dynamic_fixture(args_list: list, name_generator: callable, fixture_params: dict = None):
    if fixture_params is None:
        fixture_params = {}

    def dynamic_fixture_for_params(func):
        module = inspect.getmodule(func)
        for this_args in args_list:
            func_with_args = FunctionWithArgs(func, *this_args)
            setattr(module, name_generator(*this_args), gen_fix_outside(func_with_args, fixture_params))

        def pass_f():
            pass
        return pass_f
    return dynamic_fixture_for_params
