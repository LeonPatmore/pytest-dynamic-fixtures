import functools


def print_dec_factory(run: bool):
    def print_dec(func):
        if run:
            @functools.wraps(func)
            def surround():
                print("Starting!")
                func()
                print("Done")
            return surround
        else:
            return func
    return print_dec


@print_dec_factory(True)
def say_hi():
    print("hi")


@print_dec_factory(False)
def say_bye():
    print("bye")


if __name__ == '__main__':
    say_hi()
    say_bye()
